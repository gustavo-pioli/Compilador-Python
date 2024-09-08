EOF = "$"
ERRO = -1

ESTADOS_FINAIS = ["-1","2", "3", "5", "6", "8", "10", "11", "12", "13", "15", "16", "17", 
                "18", "19", "20", "22", "23", "26", "28", "30", "32", "35", "37", "41"]

TRANSICOES = {
        "0": {
            "transicoes": {
                "<": "1",
                ">": "4",
                "=": "7",
                "!": "9",
                "+": "11",
                "-": "12",
                "/": "13",
                "*": "14",
                "(": "17",
                ")": "18",
                ",": "19",
                ";": "20",
                ":": "21",
                "'": "24",
                " \t\n": "27",
                "{": "29",
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_": "31",
                "0123456789": "33",
            },
            "transicoes_dif": {
            },
        },
        "1": {
            "transicoes": {
                "=": "2"
            },
            "transicoes_dif": {
                "=": "3"
            },
        },
        "4": {
            "transicoes": {
                "=": "5"
            },
            "transicoes_dif": {
                "=": "6"
            }    
        },
        "7": {
            "transicoes": {
                "=": "8"
            },
            "transicoes_dif": {
            },
        },  
        "9": {
            "transicoes": {
                "=": "10"
            },
            "transicoes_dif": {
            },
        }, 
        "14": {
            "transicoes": {
                "*": "16"
            },
            "transicoes_dif": {
                "*": "15"
            }  
        },
        "21": {
            "transicoes": {
                "=": "23"
            },
            "transicoes_dif": {
                "=": "22"
            }
        },
        "24": {
            "transicoes": {
            },
            "transicoes_dif": {
                "\n": "25"
            }
        },
        "25": {
            "transicoes": {
                "'": "26"
            },
            "transicoes_dif": {
            },
        },
        "27": {
            "transicoes": {
                " \t\n": "27"
            },
            "transicoes_dif": {
                " \t\n": "28"
            }
        },
        "29": {
            "transicoes": {
                "}": "30"
            },
            "transicoes_dif": {
                "}": "29"
            }
        },
        "31": {
            "transicoes": {
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789": "31"
            },
            "transicoes_dif": {
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789": "32"
            }
        },
        "33": {
            "transicoes": {
                "0123456789": "33",
                ".": "34",
                "E": "38"
            },
            "transicoes_dif": {
                "0123456789.E": "35"
            }
        },
        "34": {
            "transicoes": {
                "0123456789": "36"
            },
            "transicoes_dif": {
            },
        },
        "36": {
            "transicoes": {
                "0123456789": "36",
                "E": "38"
            },
            "transicoes_dif": {
                "0123456789E": "37"
            }
        },
        "38": {
            "transicoes": {
                "+-": "39",
                "0123456789": "40"
            },
            "transicoes_dif": {
            },
        },
        "39": {
            "transicoes": {
                "0123456789": "40"
            },
            "transicoes_dif": {
            },
        },
        "40": {
            "transicoes": {
                "0123456789": "40"
            },
            "transicoes_dif": {
                "0123456789": "41"
            }
        }
}