# cd ../../

export CUDA_VISIBLE_DEVICES=0
# export PYTHONPATH=.

# python tools/tolmdb.py \
# /workspace/data/20200811_clean/random_deepfashion/LEAP_random_deepfashion_500_3/test_feat_deepfashion_random.npy \
# /workspace/data/20200811_clean/random_deepfashion/LEAP_random_deepfashion_500_3/test_feat_deepfashion_random.lmdb


python tools/tolmdb.py \
/workspace/data/ours/train_feat.npy \
/workspace/data/ours/train_feat.lmdb
