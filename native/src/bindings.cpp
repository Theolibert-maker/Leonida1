#include "wordscope/text_stats.hpp"

#include <cstdint>
#include <string_view>

#if defined(_WIN32)
#define WORDSCOPE_EXPORT extern "C" __declspec(dllexport)
#else
#define WORDSCOPE_EXPORT extern "C" __attribute__((visibility("default")))
#endif

// C ABI wrapper: safe to call from Python ctypes.
WORDSCOPE_EXPORT void wordscope_measure(
    const char* data,
    std::uint64_t size,
    std::uint64_t* bytes,
    std::uint64_t* lines,
    std::uint64_t* characters
) {
    if (data == nullptr || bytes == nullptr || lines == nullptr || characters == nullptr) {
        return;
    }

    const auto stats = wordscope::measure_utf8(
        std::string_view(data, static_cast<std::size_t>(size))
    );
    *bytes = stats.bytes;
    *lines = stats.lines;
    *characters = stats.characters;
}
