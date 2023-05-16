from ting_file_management.priority_queue import PriorityQueue
from pytest import fixture, raises


@fixture
def files():
	return [      
		{"qtd_linhas": 8},
		{"qtd_linhas": 3},
		{"qtd_linhas": 6},
		{"qtd_linhas": 2}
	]


@fixture
def queue():
	return PriorityQueue()


def test_basic_priority_queueing(files, queue):
	queue.enqueue(files[0])
	queue.enqueue(files[1])
	assert queue.regular_priority.queue == [files[0]]
	assert queue.high_priority.queue == [files[1]]
	assert queue.search(1) == files[0]

	queue.enqueue(files[2])
	queue.enqueue(files[3])

	assert queue.search(0) == files[1]

	with raises(IndexError, match="Índice Inválido ou Inexistente"):
		queue.search(6)

	assert queue.dequeue() == files[1]
	assert queue.dequeue() == files[3]
	assert queue.dequeue() == files[0]
	assert queue.dequeue() == files[2]
