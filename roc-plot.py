'''
function to plot ROC Curve with thresholds.
Helps with the setting of thresholds.
'''

def plot_ROC(y_true, y_score,n_thresholds=10):
    fpr, tpr, thresholds = metrics.roc_curve(y_true=y_true, y_score=y_score)
    roc_auc = metrics.auc(fpr, tpr)
    num_cuts = thresholds.shape[0]//n_thresholds
    
    plt.figure(figsize=(8,5))
    plt.plot(fpr, tpr, label="ROC Curve with AUC = %0.2f" % roc_auc)
    plt.plot(np.linspace(0,1,10), np.linspace(0,1,10), label="Diagonal")
    for x, y, txt in zip(fpr[::num_cuts], tpr[::num_cuts], thresholds[::num_cuts]):
        plt.annotate(np.round(txt,2), (x, y-0.04))

    plt.legend(loc="upper left")
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.show()
