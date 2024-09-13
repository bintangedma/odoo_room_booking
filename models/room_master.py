from odoo import models, fields, api

class RoomMaster(models.Model):
    _name = 'room.master'
    _description = 'Master Ruangan'

    name = fields.Char(string='Nama Ruangan', required=True)
    room_type = fields.Selection([
        ('small_meeting', 'Meeting Room Kecil'),
        ('large_meeting', 'Meeting Room Besar'),
        ('hall', 'Aula')],
        string='Tipe Ruangan', required=True)
    location = fields.Selection([
        ('1a', '1A'), ('1b', '1B'), ('1c', '1C'),
        ('2a', '2A'), ('2b', '2B'), ('2c', '2C')],
        string='Lokasi Ruangan', required=True)
    photo = fields.Image(string='Foto Ruangan', required=True)
    capacity = fields.Integer(string='Kapasitas Ruangan', required=True)
    description = fields.Text(string='Keterangan')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Nama Ruangan tidak boleh sama!')
    ]