/**
 * Ring buffer 环形缓冲。
 * 亦可作队列使用，在队列未满的情况下，可以持续向里面添加内容而不需要重新安排内存。提高数据操作效率。
 * 尾部索引计算：current_index = (head_index + count) % capacity（添加内容时）
 * 头部索引计算： head_index = (head + 1) % capacity；当从队列中移除头部元素时，头部向前移动一位。
 */
#ifndef __RING_BUFFER__
#define __RING_BUFFER__

#define BUFFER_LENGTH 16
#define TRUE 1
#define FALSE 0

#include <inttypes.h>

typedef int8_t bool;


typedef struct {
    int16_t head;
    int16_t count;
    int16_t capacity;
    int *data;
} RingBuffer_t;


void ringBufferInit(RingBuffer_t *buffer, int size) {
    buffer -> head = 0;
    buffer -> count = 0;
    buffer -> capacity = size;
    buffer -> data = (int *) malloc(size  * sizeof(int));
}

/**
 * free memory taken by ringbuffer on init.
 * */
void releaseBuffer(RingBuffer_t *buffer) {
    free(buffer -> data);
}

/**
 * wirte data to ringbuffer.
 * return bool:
 *  true: insert data success.
 *  false: insert data failed.
 * */
int8_t ringBufferWrite(int8_t value, RingBuffer_t buffer) {
    if(buffer.count == buffer.capacity) {
        return FALSE;
    }
    buffer.data[(buffer.head + buffer.count) % buffer.capacity] = value;
    buffer.count ++;
    return TRUE;
}

/**
 * Read data from ringbuffer. 
 * Every read operation on ringbuffer will remove the data that been read.
 * param {*data}: a pointer used to save data been read.
 * param {buffer}: a struct of type RingBuffer_t .
 * */
int8_t ringBufferRead(int8_t *data, RingBuffer_t buffer) {
    if(buffer.count == 0) return FALSE;
    *data = buffer.data[buffer.head];
    buffer.head = (buffer.head + 1) % buffer.capacity;
    buffer.count --;
    return TRUE;
}

#endif
