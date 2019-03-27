# Copyright 2018 Deep Learning Service of Huawei Cloud. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import manifest

if __name__ == '__main__':
    path = os.path.abspath('../') + "/resources/detect-test-xy-V201902220951335133.manifest"
    data_set = manifest.parse_manifest(path)
    assert data_set.get_size() == 8
    data_objects = data_set.get_sample_list()
    for data_object in data_objects:
        source = data_object.get_source()
        assert str(source).__contains__("s3://obs-ma/test/label-0220/datafiles/")
        assert str(source).__contains__(".jpg")
        usage = data_object.get_usage()
        assert usage == "TRAIN"
        annotations = data_object.get_annotations()
        for annotation in annotations:
            annotation_type = annotation.get_type()
            assert annotation_type == "modelarts/object_detection"
            annotation_name = annotation.get_name()
            assert annotation_name is None
            annotation_loc = annotation.get_loc()
            assert annotation_loc == "s3://path/menifest/data/2007_000027.xml"
            annotation_property = annotation.get_property()
            assert None == annotation_property
            annotation_create_time = annotation.get_creation_time()
            assert str(annotation_create_time).__contains__("2019-02-20 03:16")
        assert annotation.get_annotation_format() == "PASCAL VOC"
        annotation_annotated_by = annotation.get_annotated_by()
        assert annotation_annotated_by == "human"

        print(str(annotation_type) + "\t" + str(annotation_name) + "\t" + str(annotation_loc) + "\t" + str(
            annotation_property) + "\t" + str(annotation_create_time) + "\t" + str(annotation_annotated_by))

print("success")
