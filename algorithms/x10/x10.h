#ifndef X10_H
#define X10_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

void x10_hash(const char* input, char* output, uint32_t len);

#ifdef __cplusplus
}
#endif

#endif