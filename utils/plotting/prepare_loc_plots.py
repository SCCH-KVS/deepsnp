#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Copyright (C) Software Competence Center Hagenberg GmbH (SCCH)
# All rights reserved.
# -----------------------------------------------------------------------------
# This document contains proprietary information belonging to SCCH.
# Passing on and copying of this document, use and communication of its
# contents is not permitted without prior written authorization.
# -----------------------------------------------------------------------------
# Created on : 17.09.2018 $
# by : eghbal-zadeh $
# modified by : fischer $

# --- imports -----------------------------------------------------------------
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
# sns.set_style(style="dark")
# sns.set_palette("husl")

# tips = sns.load_dataset("tips")
# ax = sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
#
#
# index = ['x', 'y']
# columns = ['a','b','c']
#
# # Option 1: Set the column names in the structured array's dtype
# dtype = [('a','int32'), ('b','float32'), ('c','float32')]
# values = np.zeros(2, dtype=dtype)
# df = pd.DataFrame(values, index=index)
#
# # Option 2: Alter the structured array's column names after it has been created
# values = np.zeros(2, dtype='int32, float32, float32')
# values.dtype.names = columns
# df2 = pd.DataFrame(values, index=index, columns=columns)
#
# # Option 3: Alter the DataFrame's column names after it has been created
# values = np.zeros(2, dtype='int32, float32, float32')
# df3 = pd.DataFrame(values, index=index)
# df3.columns = columns
#
# # Option 4: Use a dict of arrays, each of the right dtype:
# df4 = pd.DataFrame(
#     {'a': np.zeros(2, dtype='int32'),
#      'b': np.zeros(2, dtype='float32'),
#      'c': np.zeros(2, dtype='float32')}, index=index, columns=columns)
#
# # Option 5: Concatenate DataFrames of the simple dtypes:
# df5 = pd.concat([
#     pd.DataFrame(np.zeros((2,), dtype='int32'), columns=['a']),
#     pd.DataFrame(np.zeros((2,2), dtype='float32'), columns=['b','c'])], axis=1)
#
# # Option 6: Alter the dtypes after the DataFrame has been formed. (This is not very efficient)
# values2 = np.zeros((2, 3))
# df6 = pd.DataFrame(values2, index=index, columns=columns)
# for col, dtype in zip(df6.columns, 'int32 float32 float32'.split()):
#     df6[col] = df6[col].astype(dtype)

# ext = 'png'
ext = 'eps'

eval_winsize = 20
# eval_winsize = 5
# eval_winsize = 10
# eval_winsize = 20


bbox_to_anchor = (0.5, 1.8)
top = 0.52

all_winsize = [40, 20, 10, 5]

methods = [r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\bl_densenet_results.txt',
           r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\bl_dil_densenet_results.txt',
           r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\bl_lstm_densenet_results.txt',
           r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\bl_vgg_results.txt',
           r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\deepsnp_finalatt_v1_results.txt',
           r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\deepsnp_finalatt_v2_results.txt',
           ## r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\deepsnp_fullatt_v1_results.txt',
           # #r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\deepsnp_fullatt_v2_results.txt',
           r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\deepsnp_noatt_v1_results.txt',
           r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\deepsnp_noatt_v2_results.txt',
           r'E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\rawcopy_results.txt']
if eval_winsize == 5 or eval_winsize == 10 or eval_winsize == 20:
    methods.extend([
        ## r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attTrue_True_v2_{}k_results.txt".format(
        ##     40, 40),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_False_v1_{}k_results.txt".format(
            40, 40),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_False_v2_{}k_results.txt".format(
            40, 40),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_True_v1_{}k_results.txt".format(
            40, 40),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_True_v2_{}k_results.txt".format(
            40, 40),
        ## r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attTrue_True_v1_{}k_results.txt".format(
        ##    40, 40)
    ])
if eval_winsize == 5 or eval_winsize == 10:
    methods.extend([
        ## r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attTrue_True_v2_{}k_results.txt".format(
        ##     20, 20),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_False_v1_{}k_results.txt".format(
            20, 20),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_False_v2_{}k_results.txt".format(
            20, 20),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_True_v1_{}k_results.txt".format(
            20, 20),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_True_v2_{}k_results.txt".format(
            20, 20),
        ## r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attTrue_True_v1_{}k_results.txt".format(
        #     20, 20),
    ])
if eval_winsize == 5:
    methods.extend([
        ## r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attTrue_True_v2_{}k_results.txt".format(
        ##     10, 10),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_False_v1_{}k_results.txt".format(
            10, 10),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_False_v2_{}k_results.txt".format(
            10, 10),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_True_v1_{}k_results.txt".format(
            10, 10),
        r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attFalse_True_v2_{}k_results.txt".format(
            10, 10),
        # # r"E:\ProjectCode\VISIOMICS\trunk\BioInf\hamid\results\loc_{}k\loc_deepsnp_attTrue_True_v1_{}k_results.txt".format(
        #     10, 10)
    ])

columns = ['Method', 'Kind', 'Fold', 'WinSize', 'F1Mac', 'F1Pos', 'PrecMac', 'PrecPos', 'RecMac', 'RecPos']
namedic = {'bl_densenet': 'DNS',
           'bl_dil_densenet': 'DILDNS',
           'bl_lstm_densenet': 'LSTM',
           'bl_vgg': 'VGG',
           'deepsnp_finalatt_v1': 'DSP1FIN',
           'deepsnp_finalatt_v2': 'DSP2FIN',
           'deepsnp_fullatt_v1': 'DSP1FUL',
           'deepsnp_fullatt_v2': 'DSP2FUL',
           'deepsnp_noatt_v1': 'DSP1NO',
           'deepsnp_noatt_v2': 'DSP2NO',
           'rawcopy': 'RC',
           'loc_deepsnp_attFalse_True_v1_{}k'.format(40): 'DSP1FIN{}k'.format(40),
           'loc_deepsnp_attFalse_True_v2_{}k'.format(40): 'DSP2FIN{}k'.format(40),
           'loc_deepsnp_attTrue_True_v1_{}k'.format(40): 'DSP1FUL{}k'.format(40),
           'loc_deepsnp_attTrue_True_v2_{}k'.format(40): 'DSP2FUL{}k'.format(40),
           'loc_deepsnp_attFalse_False_v1_{}k'.format(40): 'DSP1NO{}k'.format(40),
           'loc_deepsnp_attFalse_False_v2_{}k'.format(40): 'DSP2NO{}k'.format(40),
           #
           'loc_deepsnp_attFalse_True_v1_{}k'.format(20): 'DSP1FIN{}k'.format(20),
           'loc_deepsnp_attFalse_True_v2_{}k'.format(20): 'DSP2FIN{}k'.format(20),
           'loc_deepsnp_attTrue_True_v1_{}k'.format(20): 'DSP1FUL{}k'.format(20),
           'loc_deepsnp_attTrue_True_v2_{}k'.format(20): 'DSP2FUL{}k'.format(20),
           'loc_deepsnp_attFalse_False_v1_{}k'.format(20): 'DSP1NO{}k'.format(20),
           'loc_deepsnp_attFalse_False_v2_{}k'.format(20): 'DSP2NO{}k'.format(20),
           # #
           'loc_deepsnp_attFalse_True_v1_{}k'.format(10): 'DSP1FIN{}k'.format(10),
           'loc_deepsnp_attFalse_True_v2_{}k'.format(10): 'DSP2FIN{}k'.format(10),
           'loc_deepsnp_attTrue_True_v1_{}k'.format(10): 'DSP1FUL{}k'.format(10),
           'loc_deepsnp_attTrue_True_v2_{}k'.format(10): 'DSP2FUL{}k'.format(10),
           'loc_deepsnp_attFalse_False_v1_{}k'.format(10): 'DSP1NO{}k'.format(10),
           'loc_deepsnp_attFalse_False_v2_{}k'.format(10): 'DSP2NO{}k'.format(10),
           #
           }

method_names, folds, winsizes, f1_macs, f1_poss, prec_macs, prec_poss, rec_macs, rec_poss, method_kinds = [], [], [], [], [], [], [], [], [], []


def preprocess(data):
    return [float(d.replace('\t', '').replace('\\', '')) for d in data.split('&')[1:]]


for m in methods:
    # ubuntu
    # m_name = m.split('/')[-1].split('.')[0].split('_results')[0]
    # windows
    m_name = m.split('\\')[-1].split('.')[0].split('_results')[0]

    data = np.loadtxt(m, dtype='str', delimiter='\n')

    # initializing a 2D array for winsize x fold results
    winsize_num = 4
    fold_num = 6

    f1_mac = np.zeros((winsize_num, fold_num), dtype=np.float32)
    f1_pos = np.zeros((winsize_num, fold_num), dtype=np.float32)
    prec_mac = np.zeros((winsize_num, fold_num), dtype=np.float32)
    prec_pos = np.zeros((winsize_num, fold_num), dtype=np.float32)

    rec_mac = np.zeros((winsize_num, fold_num), dtype=np.float32)
    rec_pos = np.zeros((winsize_num, fold_num), dtype=np.float32)

    f1_mac[0, :] = preprocess(data[2])
    f1_pos[0, :] = preprocess(data[3])
    prec_mac[0, :] = preprocess(data[4])
    prec_pos[0, :] = preprocess(data[5])
    rec_mac[0, :] = preprocess(data[6])
    rec_pos[0, :] = preprocess(data[7])

    f1_mac[1, :] = preprocess(data[10])
    f1_pos[1, :] = preprocess(data[11])
    prec_mac[1, :] = preprocess(data[12])
    prec_pos[1, :] = preprocess(data[13])
    rec_mac[1, :] = preprocess(data[14])
    rec_pos[1, :] = preprocess(data[15])

    f1_mac[2, :] = preprocess(data[18])
    f1_pos[2, :] = preprocess(data[19])
    prec_mac[2, :] = preprocess(data[20])
    prec_pos[2, :] = preprocess(data[21])
    rec_mac[2, :] = preprocess(data[22])
    rec_pos[2, :] = preprocess(data[23])

    f1_mac[3, :] = preprocess(data[26])
    f1_pos[3, :] = preprocess(data[27])
    prec_mac[3, :] = preprocess(data[28])
    prec_pos[3, :] = preprocess(data[29])
    rec_mac[3, :] = preprocess(data[30])
    rec_pos[3, :] = preprocess(data[31])

    for f in range(fold_num):
        for iwin, winsize in enumerate(all_winsize):
            if winsize != eval_winsize:
                continue
            method_uid = namedic[m_name]
            method_names.append(method_uid)
            if 'loc' in m_name and 'deepsnp' in m_name:
                method_kinds.append('LOC')
            elif 'loc' not in m_name and 'deepsnp' in m_name:
                method_kinds.append('DSP')
            else:
                method_kinds.append('BL')
            folds.append(f)
            winsizes.append(winsize)

            f1_macs.append(f1_mac[iwin, f])
            f1_poss.append(f1_pos[iwin, f])

            prec_macs.append(prec_mac[iwin, f])
            prec_poss.append(prec_pos[iwin, f])

            rec_macs.append(rec_mac[iwin, f])
            rec_poss.append(rec_pos[iwin, f])

    # columns = ['Method','Fold','WinSize','F1mic','F1Mac','Precmic','PrecMac','Recmic','RecMac']
df = pd.DataFrame(
    {'Method': np.array(method_names, dtype='str'),
     'Kind': np.array(method_kinds, dtype='str'),
     'Fold': np.array(folds, dtype='int32'),
     'WinSize': np.array(winsizes, dtype='int32'),
     'F1Mac': np.array(f1_macs, dtype='float32'),
     'F1Pos': np.array(f1_poss, dtype='float32'),
     'PrecMac': np.array(prec_macs, dtype='float32'),
     'PrecPos': np.array(prec_poss, dtype='float32'),
     'RecMac': np.array(rec_macs, dtype='float32'),
     'RecPos': np.array(rec_poss, dtype='float32'),
     }, columns=columns)

# for each method, variance over folds
plt.close('all')
plt.clf()
ax = sns.barplot(x="Kind", y="F1Mac", hue="Method", data=df)
plt.legend(loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=4, fontsize='x-small')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.tick_params(axis='both', which='minor', labelsize=5)
plt.ylim([0, 100])
plt.subplots_adjust(top=top)
plt.savefig('figs/loc_eval/methods_f1_mac_{}.{}'.format(eval_winsize, ext), dpi=300)

# for each window, variance over folds
# plt.close('all')
# ax = sns.barplot(x="WinSize", y="F1Mac", hue="Method", data=df)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.3), ncol=4, fontsize = 'x-small')
# plt.savefig('figs/loc_eval/winsize_f1_mac_{}.{}'.format(eval_winsize,ext), dpi=300)
# ==================================================
plt.close('all')
plt.clf()
ax = sns.barplot(x="Kind", y="F1Pos", hue="Method", data=df)
plt.legend(loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=4, fontsize='x-small')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.tick_params(axis='both', which='minor', labelsize=5)
plt.ylim([0, 100])
plt.subplots_adjust(top=top)
plt.savefig('figs/loc_eval/methods_f1_pos_{}.{}'.format(eval_winsize, ext), dpi=300)

# for each window, variance over folds
# plt.close('all')
# ax = sns.barplot(x="WinSize", y="F1Pos", hue="Method", data=df)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15),  ncol=4, fontsize = 'x-small')
# plt.savefig('figs/loc_eval/winsize_f1_pos_{}.{}'.format(eval_winsize,ext), dpi=300)
# ==================================================
plt.close('all')
plt.clf()
ax = sns.barplot(x="Kind", y="PrecMac", hue="Method", data=df)
plt.legend(loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=4, fontsize='x-small')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.tick_params(axis='both', which='minor', labelsize=5)
plt.ylim([0, 100])
plt.subplots_adjust(top=top)
plt.savefig('figs/loc_eval/methods_prec_mac_{}.{}'.format(eval_winsize, ext), dpi=300)

# for each window, variance over folds
# plt.close('all')
# ax = sns.barplot(x="WinSize", y="PrecMac", hue="Method", data=df)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.3), ncol=4, fontsize = 'x-small')
# plt.savefig('figs/loc_eval/winsize_prec_mac_{}.{}'.format(eval_winsize,ext), dpi=300)
# ==================================================
plt.close('all')
plt.clf()
ax = sns.barplot(x="Kind", y="PrecPos", hue="Method", data=df)
plt.legend(loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=4, fontsize='x-small')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.tick_params(axis='both', which='minor', labelsize=5)
plt.ylim([0, 100])
plt.subplots_adjust(top=top)
plt.savefig('figs/loc_eval/methods_prec_pos_{}.{}'.format(eval_winsize, ext), dpi=300)
# for each window, variance over folds
# plt.close('all')
# ax = sns.barplot(x="WinSize", y="PrecPos", hue="Method", data=df)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize = 'x-small')
# plt.savefig('figs/loc_eval/winsize_prec_pos_{}.{}'.format(eval_winsize,ext), dpi=300)
# ==================================================
plt.close('all')
plt.clf()
ax = sns.barplot(x="Kind", y="RecMac", hue="Method", data=df)
plt.legend(loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=4, fontsize='x-small')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.tick_params(axis='both', which='minor', labelsize=5)
plt.ylim([0, 100])
plt.subplots_adjust(top=top)
plt.savefig('figs/loc_eval/methods_rec_mac_{}.{}'.format(eval_winsize, ext), dpi=300)
# for each window, variance over folds
# plt.close('all')
# ax = sns.barplot(x="WinSize", y="RecMac", hue="Method", data=df)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 0.3), ncol=3, fontsize = 'x-small')
# plt.savefig('figs/loc_eval/winsize_rec_mac_{}.{}'.format(eval_winsize,ext), dpi=300)
# ==================================================
plt.close('all')
plt.clf()
ax = sns.barplot(x="Kind", y="RecPos", hue="Method", data=df)
plt.legend(loc='upper center', bbox_to_anchor=bbox_to_anchor, ncol=4, fontsize='x-small')
plt.tick_params(axis='both', which='major', labelsize=5)
plt.tick_params(axis='both', which='minor', labelsize=5)
plt.ylim([0, 100])
plt.subplots_adjust(top=top)
plt.savefig('figs/loc_eval/methods_rec_pos_{}.{}'.format(eval_winsize, ext), dpi=300)

# for each window, variance over folds
# plt.close('all')
# ax = sns.barplot(x="WinSize", y="RecPos", hue="Method", data=df)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize = 'x-small')
# plt.savefig('figs/loc_eval/winsize_rec_pos_{}.{}'.format(eval_winsize,ext), dpi=300)

print('end')
