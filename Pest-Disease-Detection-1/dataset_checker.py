import os

def count_classes(annotations_dir):
    class_counts = {'Aphid': 0, 'Army Worm': 0, 'Mites': 0, 'Saw Fly': 0}
    for annotation_file in os.listdir(annotations_dir):
        if annotation_file.endswith('.txt'):
            with open(os.path.join(annotations_dir, annotation_file), 'r') as f:
                for line in f:
                    label = int(line.split()[0])  # First number is the class label
                    if label == 0:
                        class_counts['Aphid'] += 1
                    elif label == 1:
                        class_counts['Army Worm'] += 1
                    elif label == 2:
                        class_counts['Mites'] += 1
                    elif label == 3:
                        class_counts['Saw Fly'] += 1
    return class_counts

annotations_dir = 'C:\SK\Pest-Disease-Detection-1\train\labels'
class_counts = count_classes(annotations_dir)
print(class_counts)
