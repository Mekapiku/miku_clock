#!/usr/bin/env python
# coding: utf-8

import time

from pocketmiku.amidi import send
from pocketmiku.control import noteOn, noteOff, notesToMidiString
from pocketmiku.notes import stringToNotes

from Queue import Queue

task_queue = Queue();
semaphore_flag = False

def add_miku_queue(message):
	task_queue.put(message)

def process_miku():
	if not task_queue.empty() and not semaphore_flag:
		song_miku(task_queue.get(timeout=1))

def song_miku(message):
	semaphore_flag = True

	song_chars = u"おきろんおきろ"
	song_notes = stringToNotes(song_chars)
	song_keys = [62, 60, 62, 00, 62, 60, 62]
	song_lengths = [1, 1, 2, 1, 1, 1, 2]

	assert len(song_notes) == len(song_lengths) and len(song_lengths) == len(song_keys)

	print "おきろー　おきろー"
	for i in xrange(0, len(song_notes)):
		#print "Note:", song_notes[i]
		#print "Key:", song_keys[i]
		#print "Length:", song_lengths[i]
		send(notesToMidiString([song_notes[i]]))
		send(noteOn(song_keys[i]))
		time.sleep(song_lengths[i] * 0.4)
		if i == len(song_notes) - 1:
			send(noteOff(song_keys[i], 20))

	semaphore_flag = False