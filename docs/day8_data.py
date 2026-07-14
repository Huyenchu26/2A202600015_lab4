documents = [

    # 1
    """
    Apple Store

    Invoice No: INV001

    Date: 2025-06-01

    MacBook Pro
    Qty: 1
    Price: 1200 USD

    Total: 1200 USD
    """,

    # 2
    """
    Dell Technologies

    Invoice No: INV002

    Date: 2025-06-03

    Dell Monitor
    Qty: 2
    Price: 300 USD

    Total: 600 USD
    """,

    # 3
    """
    HP Store

    Date: 2025-06-05

    HP Laptop
    Qty: 1
    Price: 900 USD

    Wireless Mouse
    Qty: 1
    Price: 30 USD

    Total: 930 USD
    """,

    # 4
    """
    Lenovo

    Date: 2025-06-07

    ThinkPad X1
    Qty: 1
    Price: 1400 USD

    Total: 1400 USD
    """,

    # 5
    """
    ASUS Official Shop

    Date: 2025-06-09

    Gaming Laptop
    Qty: 1
    Price: 1500 USD

    Total: 1500 USD
    """,

    # 6
    """
    Acer

    Date: 2025-06-10

    Acer Aspire
    Qty: 2
    Price: 700 USD

    Total: 1400 USD
    """,

    # 7
    """
    Samsung Electronics

    Date: 2025-06-12

    SSD 1TB
    Qty: 3
    Price: 120 USD

    Total: 360 USD
    """,

    # 8
    """
    Logitech

    Date: 2025-06-13

    Keyboard
    Qty: 2
    Price: 50 USD

    Mouse
    Qty: 2
    Price: 25 USD

    Total: 150 USD
    """,

    # 9
    """
    Microsoft Store

    Date: 2025-06-15

    Surface Laptop
    Qty: 1
    Price: 1300 USD

    Surface Pen
    Qty: 1
    Price: 100 USD

    Total: 1400 USD
    """,

    # 10
    """
    Amazon Marketplace

    Date: 2025-06-16

    USB Cable
    Qty: 5
    Price: 8 USD

    Total: 40 USD
    """,

    # 11
    """
    Best Buy

    Date: 2025-06-18

    External HDD
    Qty: 2
    Price: 80 USD

    Total: 160 USD
    """,

    # 12
    """
    Intel Store

    Date: 2025-06-20

    Intel Core i9
    Qty: 1
    Price: 550 USD

    Total: 550 USD
    """,

    # 13
    """
    NVIDIA

    Date: 2025-06-22

    RTX 5080
    Qty: 1
    Price: 999 USD

    Total: 999 USD
    """,

    # 14
    """
    Canon

    Date: 2025-06-25

    EOS Camera
    Qty: 1
    Price: 850 USD

    Memory Card
    Qty: 2
    Price: 40 USD

    Total: 930 USD
    """,

    # 15 (document khó)
    """
    Apple Store

    MacBook Air

    Qty: 1

    Price: 999
    """
]

ground_truth = [

    {
        "vendor": "Apple Store",
        "date": "2025-06-01",
        "currency": "USD",
        "total": 1200
    },

    {
        "vendor": "Dell Technologies",
        "date": "2025-06-03",
        "currency": "USD",
        "total": 600
    },

    {
        "vendor": "HP Store",
        "date": "2025-06-05",
        "currency": "USD",
        "total": 930
    },

    {
        "vendor": "Lenovo",
        "date": "2025-06-07",
        "currency": "USD",
        "total": 1400
    },

    {
        "vendor": "ASUS Official Shop",
        "date": "2025-06-09",
        "currency": "USD",
        "total": 1500
    },

    {
        "vendor": "Acer",
        "date": "2025-06-10",
        "currency": "USD",
        "total": 1400
    },

    {
        "vendor": "Samsung Electronics",
        "date": "2025-06-12",
        "currency": "USD",
        "total": 360
    },

    {
        "vendor": "Logitech",
        "date": "2025-06-13",
        "currency": "USD",
        "total": 150
    },

    {
        "vendor": "Microsoft Store",
        "date": "2025-06-15",
        "currency": "USD",
        "total": 1400
    },

    {
        "vendor": "Amazon Marketplace",
        "date": "2025-06-16",
        "currency": "USD",
        "total": 40
    },

    {
        "vendor": "Best Buy",
        "date": "2025-06-18",
        "currency": "USD",
        "total": 160
    },

    {
        "vendor": "Intel Store",
        "date": "2025-06-20",
        "currency": "USD",
        "total": 550
    },

    {
        "vendor": "NVIDIA",
        "date": "2025-06-22",
        "currency": "USD",
        "total": 999
    },

    {
        "vendor": "Canon",
        "date": "2025-06-25",
        "currency": "USD",
        "total": 930
    },

    {
        "vendor": "Apple Store",
        "date": None,
        "currency": None,
        "total": 999
    }

]