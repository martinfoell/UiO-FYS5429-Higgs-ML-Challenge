import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import multiprocessing
import seaborn as sns
sns.set_style("darkgrid")

plt.rcParams.update({'font.size': 14})

# function to save the dataframe to a csv file
def save_csv(df, name):
    df.to_csv("../data/data_"+name+".csv", index=False)
    print(f"DataFrame saved to {name}")

# feautures from the HiggsML dataset that are not used in the training of the neural network
non_features = ['EventId',
                 'Weight',
                 'KaggleSet',
                 'KaggleWeight']

# feautures from the HiggsML dataset that every event has
features_common = ['Label',
                   'DER_mass_MMC',
                   'DER_mass_transverse_met_lep',
                   'DER_mass_vis',
                   'DER_pt_h',
                   'DER_deltar_tau_lep',
                   'DER_pt_tot',
                   'DER_sum_pt',
                   'DER_pt_ratio_lep_tau',
                   'DER_met_phi_centrality',
                   'PRI_tau_pt',
                   'PRI_tau_eta',
                   'PRI_tau_phi',
                   'PRI_lep_pt',
                   'PRI_lep_eta',
                   'PRI_lep_phi',
                   'PRI_met',
                   'PRI_met_phi',
                   'PRI_met_sumet',
                   'PRI_jet_num',
                   'PRI_jet_all_pt']

# feautures from the HiggsML dataset where only events with one or more jets have values
features_jet = ['PRI_jet_leading_pt',
                'PRI_jet_leading_eta',
                'PRI_jet_leading_phi']

# feautures from the HiggsML dataset where only events with two or more jets have values
features_jet_jet = ['DER_deltaeta_jet_jet',
                    'DER_mass_jet_jet',
                    'DER_prodeta_jet_jet',
                    'DER_lep_eta_centrality',
                    'PRI_jet_subleading_pt',
                    'PRI_jet_subleading_eta',
                    'PRI_jet_subleading_phi']

# feautures from the HiggsML dataset with the phi 
features_phi = ['PRI_tau_phi',
                'PRI_lep_phi',
                'PRI_met_phi',
                'PRI_jet_leading_phi',
                'PRI_jet_subleading_phi']


# load the dataset
raw = pd.read_csv("../data/atlas-higgs-challenge-2014-v2.csv")


# remove features that are not used for the training of the neural network
for i in non_features:
    raw.pop(i)

# convert the Label feature for signal (s) and background (b) to binary, 1 for signal and 0 for background
raw['Label'] = raw['Label'].replace({'s': 1, 'b': 0})

# fill missing values with nan 
raw = raw.replace({-999.0 : np.NaN})

# fill the DER_mass_MMC feature with the mean of the column
raw['DER_mass_MMC'] = raw['DER_mass_MMC'].fillna(raw['DER_mass_MMC'].mean())

# make array of signal and background
background = raw[raw['Label'].isin([0])]
signal = raw[raw['Label'].isin([1])]


# An overview of the datasets that are created for the training of the neural network
fillMean = raw.copy()
fillZero = raw.copy()
fillPhiRandom = raw.copy()
removeJets = raw.copy()
removePhi = raw.copy()
jets0 = raw[raw['PRI_jet_num'].isin([0])]
jets1 = raw[raw['PRI_jet_num'].isin([1])]
jets2 = raw[raw['PRI_jet_num'].isin([2, 3])]


### fillMean, the missing entries are filled with the mean of the column
fillMean = fillMean.fillna(fillMean.mean())

# fillZero, the missing entries are filled with zero
fillZero = fillZero.fillna(0)

### fillPhiRandom, the missing entries are filled with a random value between -pi and pi
lower_bound = -np.pi
upper_bound = np.pi

nan_count_sub = fillPhiRandom['PRI_jet_subleading_phi'].isna().sum()

random_values_sub = np.random.uniform(lower_bound, upper_bound, size=nan_count_sub)
fillPhiRandom['PRI_jet_subleading_phi'] = fillPhiRandom['PRI_jet_subleading_phi'].fillna(pd.Series(random_values_sub, index=fillPhiRandom.index[fillPhiRandom['PRI_jet_subleading_phi'].isna()]))

nan_count_led = fillPhiRandom['PRI_jet_leading_phi'].isna().sum()

random_values_led = np.random.uniform(lower_bound, upper_bound, size=nan_count_led)
fillPhiRandom['PRI_jet_leading_phi'] = fillPhiRandom['PRI_jet_leading_phi'].fillna(pd.Series(random_values_led, index=fillPhiRandom.index[fillPhiRandom['PRI_jet_leading_phi'].isna()]))

fillPhiRandom = fillPhiRandom.fillna(fillPhiRandom.mean())

### removeJets; remove the jet and jet_jet features 
for i in features_jet_jet + features_jet:
    removeJets.pop(i)
removeJets = removeJets.fillna(removeJets.mean())

### removePhi; remove the phi features
for i in features_phi:
    removePhi.pop(i)
removePhi = removePhi.fillna(removePhi.mean())


### jets0; remove the jet and jet_jet features for the 0 jet case
for i in features_jet + features_jet_jet:
    jets0.pop(i)

### jets1; remove the jet_jet features for the 1 jet case
for i in features_jet_jet:
    jets1.pop(i)
    
### jets2; no features are removed for the 2 and 3 jet case

# rearrange the features in the dataframe
jets0 = jets0[features_common]
jets1 = jets1[features_common + features_jet]
jets2 = jets2[features_common + features_jet + features_jet_jet]

# remove redundant features
jets0.pop('PRI_jet_num')
jets0.pop('PRI_jet_all_pt')
jets1.pop('PRI_jet_num')
jets1.pop('PRI_jet_all_pt')

# array with the datasets and their names
dfs_all = [fillMean, fillZero, fillPhiRandom, removeJets, removePhi, jets0, jets1, jets2]
names = ["fillMean", "fillZero", "fillPhiRandom", "removeJets", "removePhi", "jets0", "jets1", "jets2"]

# count the features in the datasets
for i in range(len(dfs_all)):
    print(names[i], " has ", dfs_all[i].shape[1] - 1, " feautures")
types = [fillMean, jets0, jets1, jets2]
types_names = ["All", "jets0", "jets1", "jets2"]

# calculate the number events, and the fraction of signal and background events in the datasets
for i in range(len(types)):
    signal = (types[i]['Label'] == 1).sum()
    background = (types[i]['Label'] == 0).sum()
    total = signal + background
    print(types_names[i], total, round(background/total,3), round(signal/total,3))


# save the datasets to a csv file via multiprocessing
# pool = multiprocessing.Pool(processes=len(dfs_all))
# pool.starmap(save_csv, zip(dfs_all, names))
# pool.close()
# pool.join()    

for i in range(len(features_phi)):
    plt.figure(i)
    raw[features_phi[i]].plot(kind='hist', bins=25, label=features_phi[i])
    ylim = plt.ylim()
    plt.ylim(ylim[0],ylim[1]*1.1)
    plt.xticks(np.arange(-np.pi, np.pi+np.pi/2, step=(np.pi/2)), ['-π','-π/2','0','π/2','π'])    
    plt.xlabel(r'$\phi$')
    plt.ylabel('Events')
    plt.gca().yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.gca().yaxis.get_major_formatter().set_scientific(True)
    plt.gca().yaxis.get_major_formatter().set_powerlimits((0, 0))
    plt.legend()
    plt.savefig('../plots/' + features_phi[i] + '.pdf')
    plt.show()

