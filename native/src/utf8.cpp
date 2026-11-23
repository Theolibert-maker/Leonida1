#include "wordscope/utf8.hpp"

namespace wordscope {
bool is_valid_utf8(std::string_view input) {
    std::size_t i = 0;
    while (i < input.size()) {
        const auto lead = static_cast<unsigned char>(input[i]);
        std::size_t continuation = 0;
        unsigned char second_min = 0x80;
        unsigned char second_max = 0xBF;

        if (lead <= 0x7F) {
            ++i;
            continue;
        } else if (lead >= 0xC2 && lead <= 0xDF) {
            continuation = 1;
        } else if (lead == 0xE0) {
            continuation = 2;
            second_min = 0xA0;
        } else if (lead >= 0xE1 && lead <= 0xEC) {
            continuation = 2;
        } else if (lead == 0xED) {
            continuation = 2;
            second_max = 0x9F; // Exclude UTF-16 surrogate code points.
        } else if (lead >= 0xEE && lead <= 0xEF) {
            continuation = 2;
        } else if (lead == 0xF0) {
            continuation = 3;
            second_min = 0x90;
        } else if (lead >= 0xF1 && lead <= 0xF3) {
            continuation = 3;
        } else if (lead == 0xF4) {
            continuation = 3;
            second_max = 0x8F; // Unicode ends at U+10FFFF.
        } else {
            return false;
        }

        if (i + continuation >= input.size()) return false;
        const auto second = static_cast<unsigned char>(input[i + 1]);
        if (second < second_min || second > second_max) return false;

        for (std::size_t j = 2; j <= continuation; ++j) {
            const auto byte = static_cast<unsigned char>(input[i + j]);
            if (byte < 0x80 || byte > 0xBF) return false;
        }
        i += continuation + 1;
    }
    return true;
}

std::size_t count_code_points(std::string_view input) {
    std::size_t count = 0;
    for (unsigned char byte : input) {
        if ((byte & 0xC0U) != 0x80U) ++count;
    }
    return count;
}
}
