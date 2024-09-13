from odoo import models, fields, api, exceptions, _

class RoomBooking(models.Model):
    _name = 'room.booking'
    _description = 'Pemesanan Ruangan'

    name = fields.Char(string='Nomor Pemesanan', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    room_id = fields.Many2one('room.master', string='Ruangan', required=True)
    booking_name = fields.Char(string='Nama Pemesanan', required=True)
    booking_date = fields.Date(string='Tanggal Pemesanan', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')],
        string='Status Pemesanan', default='draft')
    notes = fields.Text(string='Catatan Pemesanan')

    @api.model
    def create(self, vals):
        # Generate a unique booking number
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('room.booking') or _('New')
        # Validate unique booking name
        if self.search([('booking_name', '=', vals['booking_name'])]):
            raise exceptions.ValidationError("Nama Pemesanan tidak boleh sama.")
        # Check for overlapping bookings
        if self.search([('room_id', '=', vals['room_id']), ('booking_date', '=', vals['booking_date'])]):
            raise exceptions.ValidationError("Ruangan sudah dipesan pada tanggal tersebut.")
        return super(RoomBooking, self).create(vals)

    def action_start_booking(self):
        self.status = 'ongoing'

    def action_complete_booking(self):
        self.status = 'done'