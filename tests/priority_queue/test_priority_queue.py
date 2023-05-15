# from ting_file_management.priority_queue import PriorityQueue
# from pytest import raises


# def test_priority_queue():
#     # Setup
#     files = [
#         {"name": "file1", "lines": 10},
#         {"name": "file2", "lines": 5},
#         {"name": "file3", "lines": 7},
#         {"name": "file4", "lines": 3},
#     ]
#     queue = PriorityQueue()

#     # Test priority queueing
#     for file in files:
#         queue.enqueue(file)

#     assert queue.high_priority._data == [
#         {"name": "file4", "lines": 3},
#         {"name": "file2", "lines": 5},
#     ]
#     assert queue.regular_priority._data == [
#         {"name": "file1", "lines": 10},
#         {"name": "file3", "lines": 7},
#     ]

#     assert queue.search(0) == {"name": "file4", "lines": 3}
#     assert queue.search(1) == {"name": "file2", "lines": 5}
#     assert queue.search(2) == {"name": "file1", "lines": 10}
#     assert queue.search(3) == {"name": "file3", "lines": 7}

#     with raises(IndexError, match="Índice Inválido ou Inexistente"):
#         queue.search(4)

#     # Test dequeuing
#     assert queue.dequeue() == {"name": "file4", "lines": 3}
#     assert queue.high_priority._data == [{"name": "file2", "lines": 5}]
#     assert queue.regular_priority._data == [
#         {"name": "file1", "lines": 10},
#         {"name": "file3", "lines": 7},
#     ]

#     assert queue.dequeue() == {"name": "file2", "lines": 5}
#     assert queue.high_priority.is_empty()
#     assert queue.regular_priority._data == [
#         {"name": "file1", "lines": 10},
#         {"name": "file3", "lines": 7},
#     ]

#     assert queue.dequeue() == {"name": "file1", "lines": 10}
#     assert queue.high_priority.is_empty()
#     assert queue.regular_priority._data == [{"name": "file3", "lines": 7}]

#     assert queue.dequeue() == {"name": "file3", "lines": 7}
#     assert queue.high_priority.is_empty()
#     assert queue.regular_priority.is_empty()
