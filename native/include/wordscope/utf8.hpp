#pragma once

#include <cstddef>
#include <string_view>

namespace wordscope {
bool is_valid_utf8(std::string_view input);
std::size_t count_code_points(std::string_view input);
}
