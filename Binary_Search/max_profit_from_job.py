# You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
# difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
# worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
# Every worker can be assigned at most one job, but one job can be completed multiple times.
# For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
# Return the maximum profit we can achieve after assigning the workers to the jobs.

def get_prefix_max_profit(difficulty, profit):
    job_details = []
    for d, p in sorted(zip(difficulty, profit), key = lambda x: x[0]):
        if len(job_details) == 0:
            job_details.append((d, p))
            continue
        max_till_now = job_details[-1][1]
        job_details.append((d, max(max_till_now, p)))
    return job_details

def get_max_profit_for_worker(job_details, worker_cap):
    left, right = 0, len(job_details) - 1

    while left <= right:
        mid = (left + right)//2

        mid_value = job_details[mid]

        if worker_cap > mid_value[0]:
            left = mid + 1

        elif worker_cap < mid_value[0]:
            right = mid - 1

        else:
            i = j = mid
            while i >= 0 and job_details[i][0] == mid_value[0]:
                i -= 1
                
            while j < len(job_details) and job_details[j][0] == mid_value[0]:
                j += 1
                
            return max([j for i, j in job_details[(i + 1):j]])
    
    return 0 if job_details[right][0] > worker_cap else job_details[right][1]

def get_max_profit(workers, difficulty, profit):

    job_details = get_prefix_max_profit(difficulty, profit)

    job_details.sort(key = lambda x: x[0])
    
    total_max_profit = 0
    for worker_cap in workers:
        max_profit = get_max_profit_for_worker(job_details, worker_cap)
        total_max_profit += max_profit

    return total_max_profit



print(get_max_profit([4, 5, 6, 7], [2,4,6,8,10], [10,20,30,40,50]))


     

    
                           

    