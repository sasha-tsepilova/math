from project import count_transitive

if __name__ == "__main__":
    import time
    with open('6_task', 'w') as to_write:
        for i in range(1, 7):
            start = time.time()
            to_write.write(f'for n = {i} number of transitive relations is {count_transitive(i)} and working time {time.time() - start}'+'\n')
