{
    'name': 'Room Management',
    'version': '1.0',
    'summary': 'Manage rooms and bookings',
    'description': 'Module for managing room details and bookings.',
    'author': 'Bintang Edma',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/room_master_view.xml',
        'views/room_booking_view.xml',
        'data/sequences.xml',
    ],
    'installable': True,
    'application': True,
}