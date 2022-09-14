from odoo import api, fields, models


class PeminjamanReport(models.TransientModel):
    _name = 'ahmadlibrary.peminjamanreport'
    _description = 'New Description'

    name = fields.Char(string='Name')

    konsumen_id = fields.Many2one(
        comodel_name='res.partner',
        string='Konsumen',
        required=False)
    dari_tgl = fields.Date(
        string='Dari Tanggal',
        required=False)
    ke_tgl = fields.Date(
        string='Ke tanggal',
        required=False)

    def action_peminjaman_report(self):
        filter=[]
        konsumen_id=self.konsumen_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl

        if konsumen_id:
            filter += [('nama_peminjam', '=', konsumen_id.id)]
        if dari_tgl:
            filter += [('tgl_peminjaman', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_peminjaman', '<=', ke_tgl)]
        print(filter)
        peminjaman = self.env['ahmadlibrary.peminjaman'].search_read(filter)
        print(peminjaman)
        data = {
            'form': self.read()[0],
            'peminjamanxx': peminjaman,
        }
        print(data)
        return self.env.ref('ahmadlibrary.wizzard_peminjamanreport_pdf').report_action(self, data=data)
