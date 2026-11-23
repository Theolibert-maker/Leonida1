#include "wordscope/text_stats.hpp"

namespace wordscope {
TextStats measure_utf8(std::string_view text) {
    TextStats result{static_cast<std::uint64_t>(text.size()), 0, 0};
    bool has_content = false;

    for (unsigned char byte : text) {
        if (byte == '\n') {
            ++result.lines;
            has_content = false;
        } else {
            has_content = true;
            // Count UTF-8 code points by counting bytes that are not continuation bytes.
            if ((byte & 0xC0U) != 0x80U) {
                ++result.characters;
            }
        }
    }

    if (has_content || (!text.empty() && text.back() != '\n')) {
        ++result.lines;
    }
    return result;
}
}
