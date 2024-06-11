import os
import sys
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
sns.set_style("darkgrid")

plt.rcParams.update({'font.size': 14})

def SS(x, s, b, L):
    S1 = 0
    for i in range(len(L)):
        S1 += np.log(1 + x*s/b*(L[i]))
    return S1

def TT(x, s, b, L):
    return 2*x*s - 2*S(x, s, b, L)

modelname_time = str(sys.argv[1])
plt_show = sys.argv[2]

models = glob.glob("../plots/raw/*")

for model in models:
    timestamp = model.split("_")[-1]
    if timestamp == modelname_time+".npz":
        modelpath = model
        break

remove = ['../plots/raw/', '.npz']


modelname = modelpath
for i in remove:
    modelname = re.sub(i, '', modelname)
    print(modelname)
loaded_data = np.load(modelpath)

plot1 = False
plot2 = False
plot3 = False
plot4 = False
plot5 = False
plot6 = False

max_acc = 0
max_val_acc = 0
max_auc = 0
max_val_auc = 0


variables = loaded_data.files

print(variables)

if 'accuracy' and 'val_accuracy' in variables:
    accuracy = loaded_data['accuracy']
    val_accuracy = loaded_data['val_accuracy']
    max_acc = max(accuracy)
    max_val_acc = max(val_accuracy)
    plot1 = True

if 'loss' and 'val_loss' in variables:
    loss = loaded_data['loss']
    val_loss = loaded_data['val_loss']
    plot2 = True

if 'auc' and 'val_auc' in variables:
    auc = loaded_data['auc']
    val_auc = loaded_data['val_auc']
    max_auc = max(auc)
    max_val_auc = max(val_auc)
    plot3 = True

if 'fpc' and 'tpr' and 'auc_end' in variables:
    fpr = loaded_data['fpr']
    tpr = loaded_data['tpr']
    auc_end = loaded_data['auc_end']
    plot4 = True

if 'y_true' and 'y_pred' in variables:
    y_true = loaded_data['y_true']
    y_pred = loaded_data['y_pred']
    plot5 = True
if 'likelihood_ratio' in variables:
    L = loaded_data['likelihood_ratio']
    plot6 = True
    mu = np.linspace(0.001, 4, 100)
    s = np.sum(y_true == 0)
    b = np.sum(y_true == 1)
    mu_min = np.argmin(2*mu*(s) - 2*SS(mu, s, b, L))
    
# print("Max auc: ", max_auc)
# print("Max val auc: ", max_val_auc)
# print("Max acc: ", max_acc)
# print("Max val acc: ", max_val_acc)


datatype = modelpath.split("_")[0].split('/')[-1]
modelname = re.sub(i, '', modelname)
epochs = modelpath.split("_")[2]
nodes = modelpath.split("_")[3]
eta = modelpath.split("_")[-3]
lamda = modelpath.split("_")[-2]
time = modelpath.split("_")[-1].split(".")[0]

modeltype = "_".join([str(round(float(auc_end),3)), str(round(float(mu[mu_min]),3)), epochs, nodes, eta, lamda])

newdir = '../plots/pdf/'+datatype+'/'+modeltype+'/'
print(newdir)
isExist = os.path.exists(newdir)
if not isExist:
    os.makedirs(newdir)
    print("dir",newdir)

if plot1:
    plt.figure(0)
    plt.plot(accuracy)
    plt.plot(val_accuracy)
    plt.title(round(val_accuracy[-1],3))
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='lower right')
    plt.savefig(newdir+'accuracy.pdf')
    
if plot2:
    plt.figure(1)
    plt.plot(loss)
    plt.plot(val_loss)
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper right')
    plt.savefig(newdir+'loss.pdf')

if plot3:
    plt.figure(2)
    plt.plot(auc)
    plt.plot(val_auc)
    plt.ylabel('auc')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper right')
    plt.savefig(newdir+'auc.pdf')

if plot4:
    plt.figure(3)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot(fpr, tpr, label='ROC (area = {:.3f})'.format(auc_end))
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.legend(loc='lower right')
    plt.savefig(newdir+'roc.pdf')

n_bins = 100

def AMS(s,b):
    return np.sqrt(2*((s+b)*np.log(1+s/b)-s))
    
if plot5:
    plt.figure(4)
    n_b, bins_b, patches_b = plt.hist(y_pred[y_true==0], bins = n_bins, facecolor='blue', alpha=0.2,label="Background")
    n_s, bins_s, patches_s = plt.hist(y_pred[y_true==1], bins = n_bins, facecolor='red', alpha=0.2, label="Signal")
    B = np.sum(n_b[90:])
    S = np.sum(n_s[90:])
    print("AMS", AMS(S,B))    
    plt.axvline(x = 0.9, linestyle='dashed', color='g', label = 'cut = 0.9 ,'+ r'$Z$ = '+str(round(float(AMS(S,B)),3)))    
    plt.xlabel('TensorFlow output')
    plt.ylabel('Events')
    plt.xlim([0,1])
    plt.grid(True)
    plt.legend()
    plt.savefig(newdir+'bkg_sig.pdf')


def S(x, s, b, L):
    S1 = 0
    for i in range(len(L)):
        S1 += np.log(1 + x*s/b*(L[i]))
    return S1

def t(x, s, b, L):
    return 2*x*s - 2*S(x, s, b, L)

print(L)
if plot6:
    fig5 = plt.figure(5)
    mu = np.linspace(0.001, 4, 100)
    s = np.sum(y_true == 0)
    b = np.sum(y_true == 1)
    q = t(0, s, b, L) - t(mu[mu_min], s, b, L)
    mu_min = np.argmin(2*mu*(s) - 2*S(mu, s, b, L))        
    plt.plot(mu,  t(mu, s, b, L) - t(mu[mu_min], s, b, L), label = r'$t(\mu) - t(\hat{\mu}), Z = $'  +str(round(np.sqrt(q), 3)))
    plt.axvline(x = mu[mu_min], linestyle='dashed', color='r', label = r'$\hat{\mu}}$ = '+str(round(float(mu[mu_min]),3)))
    mu_max = np.argmax(t(mu, s, b, L) - t(mu[mu_min], s, b, L))
    plt.xlim([0, 3])
    plt.xlabel(r'$\mu$')
    plt.ylabel('Profile log-likelihood ratio')
    plt.gca().yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.gca().yaxis.get_major_formatter().set_scientific(True)
    plt.gca().yaxis.get_major_formatter().set_powerlimits((0, 0))
    plt.legend()
    plt.savefig(newdir+'likelihood.pdf')

