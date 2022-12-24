from celery import shared_task

@shared_task(bind=True)
def test_func(self):
	for i in range(10):
		print('count I : ', i)

	return "done"