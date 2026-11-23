#pragma once

#include <cstdint>
#include <string_view>

namespace wordscope {
std::uint64_t fnv1a64(std::string_view data);
}
