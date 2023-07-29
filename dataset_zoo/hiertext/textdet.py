data_root = 'data/hiertext'
cache_path = 'data/cache'

train_preparer = dict(
    obtainer=dict(
        type='AWSS3Obtainer',
        cache_path=cache_path,
        files=[
            dict(
                url='s3://open-images-dataset/ocr/train.tgz',
                save_name='hiertext_train_img.tar.gz',
                md5='00a03db54552263cea548de68a706a27',
                content=['image'],
                mapping=[['hiertext_train_img/train', 'textdet_imgs/imgs']],
            ),
            dict(
                url='https://github.com/google-research-datasets'
                '/hiertext/raw/main/gt/train.jsonl.gz',
                save_name='hiertext_annotation.jsonl.tar.gz',
                md5='681f8fa64ed1247d4ae0d68da00f6407',
                content=['annotation'],
                mapping=[[
                    'hiertext_annotation/train.jsonl', 'annotations/train.json'
                ]],
            ),
        ],
    ),
    # gatherer=dict(
    #     type="MonoGatherer", ann_name="train.json",
    #     img_dir="textdet_imgs/imgs"
    # ),
    # parser=dict(type="DetextDetAnnParser", encoding="utf-8-sig"),
    # packer=dict(type="TextDetPacker"),
    # dumper=dict(type="JsonDumper"),
)

val_preparer = train_preparer

# delete = ['annotations', 'cocotextv2_annotation', 'cocotextv2_train_img']
config_generator = dict(type='TextDetConfigGenerator')
