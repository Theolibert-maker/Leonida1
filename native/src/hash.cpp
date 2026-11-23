#include "wordscope/hash.hpp"

namespace wordscope {
std::uint64_t fnv1a64(std::string_view data) {
    constexpr std::uint64_t offset_basis = 14695981039346656037ULL;
    constexpr std::uint64_t prime = 1099511628211ULL;

    std::uint64_t hash = offset_basis;
    for (unsigned char byte : data) {
        hash ^= byte;
        hash *= prime;
    }
    return hash;
}
}
