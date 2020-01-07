import ui,console
from SQL_Connector import *

class MyTableView(object):
    def __init__(self):
        self.list = Get_Data()

        self.tv = ui.TableView()
        self.tv.name = 'アトラクション'
        self.tv.delegate = self
        self.tv.data_source = self

        nv = ui.NavigationView(self.tv)
        nv.name = '東京ディズニーランド/シー'
        nv.present('sheet')

    def tableview_did_select(self, tableview, section, row):
        tv = ui.TableView()
        tv.name = self.list[row]['name']
        sub_ds = SubTableView(self.list[row])
        tv.data_source = sub_ds
        tv.delegate  = sub_ds
        tableview.navigation_view.push_view(tv)
    def tableview_number_of_sections(self, tableview):
        return 1

    def tableview_number_of_rows(self, tableview, section):
        return len(self.list)

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        cell.text_label.text = self.list[row]['name']
        return cell

class SubTableView(object):
    def __init__(self,facility):
        self.facility = facility
        self.tv = ui.TableView()
        self.tv.delegate = self
        self.tv.data_source = self
        self.count = 0

    def tableview_did_select(self, tableview, section, row):
        tv = ui.TableView()
        tv.name = self.facility[row]['name']
        tv.delegate  = self
        tableview.navigation_view.push_view(tv)

    def tableview_number_of_sections(self, tableview):
        return 1

    def tableview_number_of_rows(self, tableview, section):
        return len(self.facility)

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        if self.count is 0:
            cell.text_label.text = '今日の待ち時間平均:'+str(int(self.facility['average']))+'分'
        if self.count is 1:
            cell.text_label.text = '現在の待ち時間:'+str(self.facility['waittime'])+'分'
        if self.count is 2:
            cell.text_label.text = '更新時刻:'+str(self.facility['time'])
        self.count = self.count + 1
        return cell

MyTableView()