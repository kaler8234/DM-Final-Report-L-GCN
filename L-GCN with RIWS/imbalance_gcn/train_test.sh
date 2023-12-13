export CUDA_VISIBLE_DEVICES=0



# python -m torch.distributed.launch --nproc_per_node=1 --master_port 21001 train_dist.py \
#         --feat_path /workspace/data/ours/train_feat.lmdb \
#         --knn_graph_path /workspace/data/ours/train_feat/knn_index_80.npy \
#         --density_path /workspace/data/ours/train_density.npy \
#         --label_path /workspace/data/ours/train_label.npy \
#         --logs-dir /workspace/data/ours/result --print_freq 20 --workers 0 \
#         --rand_val 0 --rand_twice 0 --is_density 0 --clique_size 0 --batch_size 16 \
#         --lr 0.01 --epochs 10 --features 512 --k-at-hop 5 5  --active_connection 5 \
#         --model_drop gcn --block_size 3 --drop_prob 0.7 \
#         --loss normal --ratio 0.5 --gamma 2 --alpha 0.75 \
#         --mode sup | tee /workspace/data/ours/result/log.out



python -u -m torch.distributed.launch --nproc_per_node=1 --master_port 21111 test_dist.py \
        --val_feat_path /workspace/data/ours/test_feat.lmdb \
        --val_knn_graph_path /workspace/data/ours/test_feat/knn_index_80.npy \
        --val_label_path /workspace/data/ours/test_label.npy \
        --checkpoint /workspace/data/ours/result/epoch_10.ckpt --batch_size 16 --max_size 50 --prop_step 0.5 \
        --features 512 --workers 1 --print_freq 20  --k-at-hop 5 5 \
        --active_connection 5 | tee -a /workspace/data/ours/result/eval.log