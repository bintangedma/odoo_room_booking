from odoo import http
from odoo.http import request

class RoomBookingAPI(http.Controller):

    @http.route('/api/booking_status/<int:booking_id>', type='json', auth='public', methods=['GET'])
    def get_booking_status(self, booking_id):
        booking = request.env['room.booking'].sudo().browse(booking_id)
        if not booking:
            return {'error': 'Booking not found'}
        return {
            'booking_id': booking.id,
            'booking_name': booking.booking_name,
            'status': booking.status
        }