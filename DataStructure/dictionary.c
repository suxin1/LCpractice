// #include "dictionary.h"
#include "hashtable.h"
// #include "logger.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#ifdef DMALLOC
#include "dmalloc.h"
#endif

Dictionary *dictionary_construct() {

	Dictionary *dictionary = NULL;

	/*
     * Allocate space for the object and set all fields to zero.
     */
	dictionary = calloc(1, sizeof(Dictionary));
	
	if (dictionary == NULL) {
        return NULL;
    }

    /*
     * Instantiate an internal hash table to hold the dictionary entries.
     *
     * FIXME: This number at the moment is rather arbitrary (but large).
     *        When I implement automatic growing in the hash table, this
     *        will be less important (and should probably be smaller)
     */
    dictionary->table = hash_table_construct(2000);

    if (dictionary->table == NULL) {
        return NULL;
    }
		
	return dictionary;
}

void dictionary_destroy(Dictionary *dictionary) {
     
	if (dictionary == NULL) {
        return;
    }
		
    /*
     * FIXME: Remove all elements from the hash table and free them, 
     *        before deleting the hash table.
     */
    if (dictionary->table != NULL) {
        hash_table_destroy(dictionary->table);
    }

	free(dictionary);

}

void dictionary_add_entry(Dictionary *dictionary, 
                          const char *key, const char *value) {

    int hash_code = -1;

	if (dictionary == NULL) {
        return;
    }

    if (key == NULL || key[0] == 0) {
        return;
    }

    /*
     * Generate a unique hash code for the key
     */
    hash_code = hash_table_get_hash_code_from_string(key);

    /*
     * Make a copy of the entry value so that it won't get changed
     */
    if (value != NULL) {
        value = strdup(value);
    }

    /*
     * Add the copy of the entry value to the hash table
     */
    hash_table_add_element(dictionary->table, value, hash_code);

}

const char *dictionary_get_entry(Dictionary *dictionary, const char *key) {

    const char *value = NULL;
    int hash_code = -1;

    if (dictionary == NULL) {
        return NULL;
    }

    if (key == NULL || key[0] == 0) {
        return NULL;
    }

    /*
     * Generate a unique hash code for the key
     */
    hash_code = hash_table_get_hash_code_from_string(key);

    /*
     * Retrieve the entry value from the hash table
     */
    value = hash_table_get_element(dictionary->table, hash_code);

    return value;
}