from datasets import load_dataset, DatasetDict, Dataset
from datasets import Audio

data_files = {'train': 'train_with_path.csv', 'test': 'test_with_path.csv'}


common_voice = load_dataset('csv', data_files=data_files, split=DatasetDict({'train': 'train', 'test': 'test'}))
common_voice['train'] = common_voice['train'].rename_column('Sentences', 'sentence')
common_voice['test'] = common_voice['test'].rename_column('Sentences', 'sentence')

print(common_voice['test'])

trainset = Dataset.from_dict({"audio": common_voice['train']['path']}).cast_column("audio", Audio())
testset = Dataset.from_dict({"audio": common_voice['test']['path']}).cast_column("audio", Audio())

print(testset)

trainset = trainset.add_column('path', common_voice['train']['path'])
common_voice['train'] = trainset.add_column('sentence', common_voice['train']['sentence'])

testset = testset.add_column('path', common_voice['test']['path'])
common_voice['test'] = testset.add_column('sentence', common_voice['test']['sentence'])


print(common_voice['test'][0])


