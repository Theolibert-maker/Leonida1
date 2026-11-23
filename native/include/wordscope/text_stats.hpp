#pragma once

#include <cstddef>
#include <cstdint>
#include <string_view>

namespace wordscope {
struct TextStats {
    std::uint64_t bytes;
    std::uint64_t lines;
    std::uint64_t characters;
};

TextStats measure_utf8(std::string_view text);
}
