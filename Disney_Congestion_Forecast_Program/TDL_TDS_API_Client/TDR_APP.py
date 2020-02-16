import ui,console,APP_Plot,API_List
import SQL_Connector_PLT as SCP
import SQL_Connector as SC

class MyTableView(object):
    def __init__(self):
        self.list,self.time = SC.Get_Data()
        self.tv = ui.TableView()
        if len(self.list) == 0:
            self.tv.name = '閉園中'
        else:
            self.tv.name = self.time[0][0]+':'+'ランド'+str(self.time[0][1])[:-3]+'-'+str(self.time[0][2])[:-3]+' シー'+str(self.time[1][1])[:-3]+'-'+str(self.time[1][2])[:-3]
        self.tv.delegate = self
        self.tv.data_source = self

        nv = ui.NavigationView(self.tv)
        nv.name = '東京ディズニーランド/シー待ち時間解析'
        nv.present('fullscreen')

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
        self.data = API_List.Get_API_Fac_Inf()
        self.list = ['運営情報:'+str(self.facility['op_status'])]
        if self.facility['op_status'] != '運営・公演中止':
            self.list.append('営業時間:'+str(self.facility['op_s'])[:-3]+'~'+str(self.facility['op_e'])[:-3])
            if self.facility['op_status'] != '案内終了' and self.facility['op_status'] != 'ファストパスエントランスのみ案内中':
                self.list.append('今日の待ち時間平均:'+str(int(self.facility['average']))+'分')
                self.list.append('現在の待ち時間:'+str(self.facility['waittime'])+'分')
                if self.facility['fp_status'] != None:
                    self.list.append('ファストパス情報:'+str(self.facility['fp_status']))
                    if self.facility['fp_status'] == '発行中':
                        self.list.append('ファストパス開始時刻:'+str(self.facility['fp_s'])[:-3])
                        self.list.append('ファストパス終了時刻:'+str(self.facility['fp_e'])[:-3])
        self.list.append('更新時刻:'+str(self.facility['time']))
        self.tv = ui.TableView()
        self.tv.delegate = self
        self.tv.data_source = self
        self.count = 0
    
    def tableview_did_select(self, tableview, section, row):
        if row != 2:
            tv = APP_Plot.MyClass(SCP.Get_Data(self.facility['ID'])[0],SCP.Get_Data(self.facility['ID'])[1],int(self.facility['average']),self.facility['name'])
            tv.name = '待ち時間変化グラフ'
            tableview.navigation_view.push_view(tv)
            
    def tableview_number_of_sections(self, tableview):
        return 1

    def tableview_number_of_rows(self, tableview, section):
        return len(self.list)

    def tableview_cell_for_row(self, tableview, section, row):
        cell = ui.TableViewCell()
        cell.text_label.text = self.list[row]
        return cell


MyTableView()
