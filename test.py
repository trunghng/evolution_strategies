import es
from test_functions import rastrigin, rosenbrock, schaffer
import numpy as np
import matplotlib.pyplot as plt
from plot import Plot
from tqdm import trange


if __name__ == '__main__':
    n_runs = 100
    # n_runs = 1
    np.random.seed(13)
    # ns = [2, 5, 10, 20]
    ns = [2, 5]
    # popsizes = []
    popsizes = [5, 7, 10, 14, 20, 32, 50]

    np.set_printoptions(precision=16)
    record = dict()

    for n in ns:
        for popsize in popsizes:
            fstop_count = 0
            for _ in trange(n_runs):
                mu = np.random.uniform(1, 5, n)
                A = np.identity(n)
                ftarget = 1e-8
                # figsize = (10, 10)
                # img_basename = './images/cmaes-rastrigin'
                # x1 = np.linspace(-500, 500, num=100)
                # x2 = np.linspace(-500, 500, num=100)
                f = rastrigin
                # plot = Plot(figsize, img_basename, x1, x2, f)
                es_ = es.xNES(mu, A, ftarget=ftarget, popsize=popsize)
                # es_ = es.CMAES(xstart, sigma)


                while True:
                    X = es_.ask()
                    fitness_list = np.array([-f(X[:, i]) for i in range(X.shape[1])])
                    es_.tell(fitness_list)
                    result = es_.result()
                    # current_iter = result['count_iter']
                    # if current_iter % 5 == 0:    
                    #     plot.contour()
                    #     plot.point(xstart, 'black')
                    #     plot.point(result['best_sol'], 'red')
                    #     plot.point(result['solutions'], 'blue', alpha=0.3)
                    #     plot.save(f'iter{current_iter}')
                    #     plot.clf()

                    if es_.stop():
                        if -result['best_val'] <= ftarget:
                            fstop_count += 1
                        # print()
                        # print(result['best_sol'])
                        # print('best_val:', -result['best_val'])
                        # print(result['solutions'])
                        # print('count_eval:', result['count_eval'])
                        # print('Terminated due to:', es_.stop())
                        # print(es_.result())
                        # plot.contour()
                        # plot.point(xstart, 'black')
                        # plot.point(result['best_sol'], 'red')
                        # plot.point(result['solutions'], 'blue', alpha=0.5)
                        # plot.gif('end')
                        # plot.close()
                        break

            print(f'n={n}, popsize={popsize}, fstop_count={fstop_count}')
            record[f'n={n},popsize={popsize}'] = fstop_count

print(record)

