import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import project.config as config
import os
import pdb

plt.style.use("fivethirtyeight")


def feature_importance(imps, parameters, output_importance_path, base_label="test"):
    # MANUAL WORK FOR NOW, add the vector from the printed output or log file if that is available.
    # instance 1, instance 2, instance 3 - readwrite-ratio: 10/90, 50/50, 90/10
    # imps = [
    #     [
    #         0.15646801973871374,
    #         0.07849529595255675,
    #         0.03081753585534445,
    #         0.07200575817142718,
    #         0.02927159571575296,
    #         0.026044780576225716,
    #         0.025541332606416372,
    #         0.2987987429907389,
    #         0.18789163057738495,
    #         0.04941317169401913,
    #         0.004518043369831316,
    #         0.01635879279779299,
    #         0.02437529995379549,
    #     ],
    #     [
    #         0.135681964840895,
    #         0.04938281010682532,
    #         0.02216466392568001,
    #         0.025963158673754608,
    #         0.012985602520763412,
    #         0.012552424326845429,
    #         0.0009743238799267961,
    #         0.3790891677648175,
    #         0.1130446060014296,
    #         0.2444522259290513,
    #         0.0003697043007849122,
    #         0.0014500691120544163,
    #         0.001889278617171676,
    #     ],
    #     [
    #         0.05553312218076969,
    #         0.12197702426967763,
    #         0.0030903626726099184,
    #         0.05001029970879262,
    #         0.019016875816268854,
    #         0.0035780510026195227,
    #         0.01515037341291004,
    #         0.3424995409556675,
    #         0.17796203939281888,
    #         0.1734514627436494,
    #         0.005661247358725462,
    #         0.00845414303708673,
    #         0.023615457448403734,
    #     ],
    # ]

    threshold = 0.02
    colors = ["firebrick", "forestgreen", "royalblue"]
    hatches = ["\\", "-", "/"]
    labels = [f"{base_label} - " + str(x) for x in range(1, 4)]

    #################### PLOT FEATURE IMPORTANCES ####################
    fig, ax = plt.subplots()
    width = 0.3
    r1 = np.arange(len(parameters))
    r2 = [x + width for x in r1]
    r3 = [x + width for x in r2]
    r = [r1, r2, r3]
    for i in range(len(imps)):
        ax.bar(
            r[i],
            imps[i],
            width=width,
            color=colors[i],
            # hatch=hatches[i],
            edgecolor="white",
            label=labels[i],
        )
    # Plot threshold
    # ax.plot([0., len(parameters)], [threshold, threshold], "k")
    ax.axhline(y=threshold, linewidth=1, color="k", label=f"{threshold*100}%-level")

    ax.set_ylabel("Importance weight")
    ax.set_xticks([t + width for t in range(len(parameters))])
    ax.set_xticklabels(parameters, rotation=90)
    ax.legend()
    fig.savefig(output_importance_path, bbox_inches="tight")
    plt.close()


def latencies():
    default_rl = []
    default_wl = [701.03, 704.09, 707.44]

    best_rl = []
    best_wl = [676.05, 719.70, 662.95]

    std = [np.std(default_wl), np.std(best_wl)]
    values = [np.mean(default_wl), np.mean(best_wl)]

    error = np.int0([std[0], std[1]])
    plt.figure(figsize=(10, 6))
    # plt.suptitle('RocksDB', size=20)
    plt.title("RRWR (r/w - 50/50)", size=17)
    # plt.grid(axis='y',zorder=0)
    plt.ylim((0, 800))
    plt.ylabel("Write latency" + r"($\mu$s)", size=15)
    plt.bar(
        np.arange(2),
        height=values,
        color=["grey", "firebrick"],
        yerr=error,
        capsize=7,
        zorder=3,
        width=0.6,
    )
    plt.xticks(np.arange(2), ["Default", "DBtune"], size=15)

    for index, value in enumerate(values):
        plt.text(index - 0.065, value + 1000, str(value), size=15)

    plt.show()


def throughput():
    optimization_cycle = 2
    output_ops_path = "snic-test/test_50_50.png"

    workload_files = [f"snic-test/RUN_1_{i}.csv" for i in range(1, 11)]

    # Parse TPS from csv files
    y = []
    means_with_errors = []
    for file in workload_files:
        df = pd.read_csv(file, header=None, names=["Throughput", "Latency"])
        tps = df.iloc[:, 0].values
        # Update with only best so far
        prev = tps[0]
        for i in range(1, len(tps)):
            if tps[i] < prev:
                tps[i] = prev
            prev = tps[i]

        y.append(tps)

    # add mean with error bars
    res = []
    means = np.mean(y, axis=0)
    maxs = np.max(y, axis=0)
    mins = np.min(y, axis=0)
    res.append(means)
    res.append(maxs)
    res.append(mins)
    pdb.set_trace()

    #################### PLOT THROUGHPUTS ####################
    iterations = len(y[0])
    x = np.linspace(0, iterations, num=iterations)
    colors = ["firebrick", "forestgreen", "royalblue", "lightgray"]
    labels = ["10/90", "50/50", "90/10"]
    # legend_locs = [7, 1, 7]
    fig, ax1 = plt.subplots()

    # plot additional as gray lines, and contrast the mean line with a strong color
    # for i in range(len(workload_y)-1):
    #     plt.plot(x, workload_y[i], color=colors[-1])

    upper_bound = res[1]
    upper_error = np.abs(res[1] - res[0])
    lower_bound = res[2]
    lower_error = np.abs(res[0] - res[2])
    # plt.errorbar(x, means_with_errors[workload_ind]
    #              [0], yerr=[lower_error, upper_error], color=colors[0], label='HyperMapper', ecolor='lightsteelblue')
    ax1.plot(x, res[0], color=colors[0], label="DBtune")
    ax1.fill_between(x, lower_bound, upper_bound, color="b", alpha=0.1)
    ax1.axhline(y=res[0][0], linewidth=1, color="k", label="Default")
    ax1.set_ylabel("Throughput (ops/s)")
    ax1.set_xlabel("Optimizer iteration")
    ax1.set_title("SNIC test with RRWR - 50/50")
    # Legend for hidden plot for latency so we get one legend
    # ax1.plot(np.nan, '-r', color=colors[2], label='Read latency')
    fig.savefig(f"{output_ops_path}", bbox_inches="tight")
    # ax1.close()
    ax1.cla()


def throughput_multiple():
    optimization_cycle = 2
    output_ops_path = f"optimizer-output/{optimization_cycle}_throughput"
    files = [
        f"optimizer-output/{optimization_cycle}_" + file
        for file in [
            "optimizer_5_10-90.csv",
            "optimizer_5_50-50.csv",
            "optimizer_5_90-10.csv",
        ]
    ]

    latency_cycle = 1
    latency_files = [
        f"optimizer-output/latencies_pruned_{latency_cycle}_" + file
        for file in ["10-90.md", "50-50.md", "90-10.md"]
    ]

    additional = True
    additional = {
        2: [
            f"optimizer-output/{optimization_cycle}_" + file
            for file in [
                "optimizer_6_10-90.csv",
                "optimizer_6_50-50.csv",
                "optimizer_7_90-10.csv",
            ]
        ],
        3: [
            f"optimizer-output/{optimization_cycle}_" + file
            for file in [
                "optimizer_7_10-90.csv",
                "optimizer_7_50-50.csv",
                "optimizer_7_90-10.csv",
            ]
        ],
    }

    # Parse TPS from csv files
    y_store = []
    means_with_errors = []
    indices_max = [[], [], []]
    # best_workload_indices = [[0], [0], [0]]
    for workload_ind, file in enumerate(files):
        y = []
        df = pd.read_csv(file)
        tps = -1 * df.loc[:, "Throughput"]
        y.append(tps.values)
        # save index of max for latency plot in plot_latency.py
        indices_max[workload_ind].append(np.argmax(tps) + 1)

        # additional throughput columns
        if additional:
            for sequence in additional.items():
                add_df = pd.read_csv(sequence[1][workload_ind])
                tps = -1 * add_df.loc[:, "Throughput"]
                y.append(tps.values)
                # save index of max for latency plot in plot_latency.py
                indices_max[workload_ind].append(np.argmax(tps) + 1)

        # We want to see the convergence, so we transform the throughput values to show only BEST SO FAR
        best_index = 0
        for iter_1, y_i in enumerate(y):
            for i in range(1, len(y_i)):
                if y_i[i - 1] > y_i[i]:
                    # if iter_1 == 2:
                    #     best_workload_indices[workload_ind].append(
                    #         best_workload_indices[workload_ind][-1])
                    y_i[i] = y_i[i - 1]
                # else:
                # if iter_1 == 2:
                #     best_workload_indices[workload_ind].append(i)

        # add mean with error bars
        res = []
        means = np.mean(y, axis=0)
        maxs = np.max(y, axis=0)
        mins = np.min(y, axis=0)
        res.append(means)
        res.append(maxs)
        res.append(mins)
        means_with_errors.append(res)

        # Print interesting stuff
        max_def = np.max([x[0] for x in y])
        min_def = np.min([x[0] for x in y])
        variation = (max_def - min_def) / min_def
        perf_incr = (means[-1] - means[0]) / means[0]
        print(f"Variation of default in workload {workload_ind}: {variation}")
        print(
            f"Performance increase in mean curve in workload {workload_ind}: {perf_incr}"
        )
        print(f"Mean Default in workload {workload_ind}: {means[0]}")
        print(f"Mean Best in workload {workload_ind}: {means[-1]}")
        print(
            f"Best TPS values in workload {workload_ind}: {y[0][-1]}, {y[1][-1]}, {y[2][-1]}\n"
        )

        # store workload throughputs
        y_store.append(y)

    #################### PLOT THROUGHPUTS ####################
    iterations = len(y_store[0][0])
    x = np.linspace(0, iterations, num=iterations)
    colors = ["firebrick", "forestgreen", "royalblue", "lightgray"]
    labels = ["10/90", "50/50", "90/10"]
    legend_locs = [7, 1, 7]
    fig, ax1 = plt.subplots()
    # ax2 = ax1.twinx()

    for workload_ind, workload_y in enumerate(y_store):
        workload_y = [y_i for y_i in workload_y]

        # plot additional as gray lines, and contrast the mean line with a strong color
        # for i in range(len(workload_y)-1):
        #     plt.plot(x, workload_y[i], color=colors[-1])

        upper_bound = means_with_errors[workload_ind][1]
        upper_error = np.abs(
            means_with_errors[workload_ind][1] - means_with_errors[workload_ind][0]
        )
        lower_bound = means_with_errors[workload_ind][2]
        lower_error = np.abs(
            means_with_errors[workload_ind][0] - means_with_errors[workload_ind][2]
        )
        # plt.errorbar(x, means_with_errors[workload_ind]
        #              [0], yerr=[lower_error, upper_error], color=colors[0], label='HyperMapper', ecolor='lightsteelblue')
        ax1.plot(x, means_with_errors[workload_ind][0], color=colors[0], label="DBtune")
        ax1.fill_between(x, lower_bound, upper_bound, color="b", alpha=0.1)
        ax1.axhline(
            y=means_with_errors[workload_ind][0][0],
            linewidth=1,
            color="k",
            label="Default",
        )
        ax1.set_ylabel("Throughput (ops/s)")
        ax1.set_xlabel("Optimizer iteration")
        ax1.set_title(fr"RRWR - {labels[workload_ind]} at $\alpha = 2\%$")
        # Legend for hidden plot for latency so we get one legend
        # ax1.plot(np.nan, '-r', color=colors[2], label='Read latency')
        ax1.legend(loc=legend_locs[workload_ind])

        # ax2.plot(x, l_workloads[workload_ind],
        #          color=colors[2], label='Read latency')
        # ax2.set_ylabel(r'Read latency ($\mu$s)')
        # ax2.legend()
        fig.savefig(
            f"{output_ops_path}_{workload_ind+1}_db_tune.pdf", bbox_inches="tight"
        )
        # ax1.close()
        ax1.cla()
        # ax2.cla()
