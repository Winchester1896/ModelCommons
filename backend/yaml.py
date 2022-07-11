# Regular imports
from copy import deepcopy

# Yaml loaders and dumpers
from ruamel.yaml.main import \
    round_trip_load as yaml_load, \
    round_trip_dump as yaml_dump

# Yaml commentary
from ruamel.yaml.comments import \
    CommentedMap as OrderedDict, \
    CommentedSeq as OrderedList

# For manual creation of tokens
from ruamel.yaml.tokens import CommentToken
from ruamel.yaml.error import CommentMark
import ruamel.yaml
import sys
# Globals
# Number of spaces for an indent 
INDENTATION = 2 
# Used to reset comment objects
tsRESET_COMMENT_LIST = [None, [], None, None]
yaml = ruamel.yaml.YAML()
yaml.preserve_quotes=True
yaml.indent=2


def create_yaml_file():
    example_data_sheet = OrderedDict({
            "data title": "soybean leaf defoliation data set",
            "physical properties": OrderedDict({
                "ownership": "Zichen Zhang",
                "data purpose": "image classification",
                "data informatioin": OrderedDict({
                    "number of classes": "2",
                    "data size": "97395",
                    "class list": OrderedDict({
                        "0": "healthy leaf",
                        "1": "defoliated leaf"}),
                    "data structure": OrderedDict({
                        "training": OrderedDict({
                            "0": "46676",
                            "1": "20441"
                        }),
                        "validation": OrderedDict({
                            "0": "14073",
                            "1": "5992"
                        }),
                        "testing": OrderedDict({
                            "0": "6730",
                            "1": "3483"
                        })
                    })
                }),
                "location": OrderedDict({
                    "dataverse": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VJMBUO",
                    "github": "https://github.com/Winchester1896/DefoNet"}),
                "data format": "image", 
                "data status": "ready to use",
                "keywords": OrderedList(["soybean", "defoliation", "neural", "network", "training", "agriculture"]),
                "MD5": "f4ef619cb585540986e44b8d1733dd7b",
                "data version": 1.0,
                "related publication": "https://www.sciencedirect.com/science/article/pii/S0168169921006992?casa_token=9spxcG3NzOIAAAAA:fOOFGUzZIeoGXXa5jVsUzBMkECGhr_xW-xw_Seaugw65BMfL2xl9Je5A3HB2p1C9my8Da0WAPxI"
            }),
            "model properties": OrderedDict({
                "defonet": OrderedDict({
                    "ownership": "Zichen Zhang",
                    "location": OrderedDict({
                        "docker": OrderedList(["zichenzhang/defonet-train:1.0",
                            "zichenzhang/defonet-predict:latest"]),
                        "github": "https://github.com/Winchester1896/DefoNet"
                    }),
                    "related publication": "https://www.sciencedirect.com/science/article/pii/S0168169921006992?casa_token=9spxcG3NzOIAAAAA:fOOFGUzZIeoGXXa5jVsUzBMkECGhr_xW-xw_Seaugw65BMfL2xl9Je5A3HB2p1C9my8Da0WAPxI",
                    "performance": OrderedDict({
                        "accuracy": "92.65%",
                        "recall": "90.93%",
                        "precision": "87.92%",
                        "training devices": "nvidia rtx 2080 ti",
                        "number of devices": "1",
                        "training time": "504mins",
                        "budget used": "$00"
                    }),
                }),
                "vgg16": OrderedDict({
                    "ownership": "x",
                    "location": OrderedDict({
                        "docker": OrderedList(["x",
                            "x"]),
                        "github": "x"
                    }),
                    "related publication": "x",
                    "performance": OrderedDict({
                        "accuracy": "88.49%",
                        "recall": "80.65%",
                        "precision": "84.84%",
                        "training devices": "nvidia rtx 2080 ti",
                        "number of devices": "1",
                        "training time": "4183mins",
                        "budget used": "$00"
                    }),
                }),
                "resnet50": OrderedDict({
                    "ownership": "x",
                    "location": OrderedDict({
                        "docker": OrderedList(["x",
                            "x"]),
                        "github": "x"
                    }),
                    "related publication": "x",
                    "performance": OrderedDict({
                        "accuracy": "87.91%",
                        "recall": "77.92%",
                        "precision": "85.35%",
                        "training devices": "nvidia rtx 2080 ti",
                        "number of devices": "1",
                        "training time": "3097mins",
                        "budget used": "$00"
                    }),
                })
                
            })
    })

    example_data_sheet.get("physical properties").yaml_add_eol_comment("ready to use or raw data", "data status")
    # Dump the yaml file
    yaml.dump(example_data_sheet, sys.stdout)

    with open("sample_datasheet.yml", "w") as f:
        yaml.dump(example_data_sheet, f)
    f.close()

