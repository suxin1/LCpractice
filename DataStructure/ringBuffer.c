#ifndef __RING_BUFFER__
#define __RING_BUFFER__

#define BUFFER_LENGTH 16
#define TRUE 1
#define FALSE 0

#include <inttypes.h>

typedef struct {
    int16_t Head;
    int16_t count;
    int16_t capacity;
    int8_t data[BUFFER_LENGTH];
}RingBuffer_t;

void ringBufferInit(RingBuffer_t buffer) {
    buffer.Head = 0;
    buffer.count = 0;
    buffer.capacity = BUFFER_LENGTH;
}

int8_t ringBufferWrite(int8_t value, RingBuffer_t buffer) {
    if(buffer.count == buffer.capacity) {
        return FALSE;
    }
    buffer.data[(buffer.Head + buffer.count) % buffer.capacity] = value;
    buffer.count ++;
    return TRUE;
}

int8_t ringBufferRead(int8_t *data, RingBuffer_t buffer) {
    if(buffer.count == 0) return FALSE;
    *data = buffer.data[buffer.Head];
    buffer.Head = (buffer.Head + 1) % buffer.capacity;
    buffer.count --;
    return TRUE;
}

#endif
