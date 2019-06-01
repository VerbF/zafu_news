# coding=utf-8

import codecs
import os

def write_history_file(file_path,record_list):
    history_file = open(file_path,'w', encoding='utf8')
    for record in record_list:
        history_file.write(record+'\n')
    history_file.close()

def read_history_file(file_path):
    history_file = open(file_path,'r',encoding='utf8')
    record_list = history_file.readlines()
    return record_list

def get_file_len(file_path):
    return len(open(file_path, encoding='utf8').read()) 

def is_empty(file_path):
    history_len = get_file_len(file_path)
    return history_len == 0 or history_len == 1 or history_len == 3