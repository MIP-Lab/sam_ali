# dataset settings
dataset_type = 'Dataset3dsam'
data_root = '/nobackup/mip_eecs/sud/reg_cochlear_new/data_128_inAtlas_99clip/'
# anno_root = '/data/sdb/user/mmdet/data/'
train_pipeline = [
    dict(type='LoadTioImage'),
    dict(type='RescaleIntensity', out_min_max=(0, 255), in_min_max=(-1, 1)),
    dict(type='ComputeAugParam', standard_spacing=(2, 2, 2), patch_size=(64, 64, 32))
]
test_pipeline = [
    dict(type='LoadTioImage'),
    dict(type='RescaleIntensity')
]
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        data_dir=data_root + 'train/Pre_img_2mm/',
        index_file=data_root + 'reg_cochlear_sam_train.csv',
        pipeline=train_pipeline,
    ),
    # val=dict(
    #     type=dataset_type,
    #     data_dir=data_root + 'nii/',
    #     index_file=data_root + 'val.csv',
    #     pipeline=test_pipeline,
    # ),
    # test=dict(
    #     type=dataset_type,
    #     data_dir=data_root + 'nii/',
    #     index_file=data_root + 'test.csv',
    #     pipeline=test_pipeline,
    # ),
)
evaluation = dict(interval=1)
