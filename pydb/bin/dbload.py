import re
from datetime import date

from main.bin.appfunc import dayRecFn, respStatusFn, errDict, dbConnFn, dbStatusCheck
from pydb.models import Dbsvcupd, AppErr


class Dbload:
    def __init__(self):
        dbStatusCheck()
        dbConnFn()
        self.regexstr = "[^_-0-9a-zA-ZА-я]+"

        try:
            today = date.today()
            if (today.month % 2) == 0:
                self.tbldict = {
                    "tbluwln": Db110102,
                    "tblowln": Db110202,
                    "tblufrt": Db120102,
                    "tblofrt": Db120202,
                    "tblugls": Db130102,
                    "tblogls": Db130202,
                    "tbluspc": Db140102,
                    "tblospc": Db140202,
                    "tbluera": Db150102,
                    "tbloera": Db150202,
                    "tbluwnl": Db160102,
                    "tblownl": Db160202,
                }
            else:
                self.tbldict = {
                    "tbluwln": Db110101,
                    "tblowln": Db110201,
                    "tblufrt": Db120101,
                    "tblofrt": Db120201,
                    "tblugls": Db130101,
                    "tblogls": Db130201,
                    "tbluspc": Db140101,
                    "tblospc": Db140201,
                    "tbluera": Db150101,
                    "tbloera": Db150201,
                    "tbluwnl": Db160101,
                    "tblownl": Db160201,
                }

            self.tbldict["tbluwln"].objects.all().delete()
            self.tbldict["tblowln"].objects.all().delete()
            self.tbldict["tblufrt"].objects.all().delete()
            self.tbldict["tblofrt"].objects.all().delete()
            self.tbldict["tblugls"].objects.all().delete()
            self.tbldict["tblogls"].objects.all().delete()
            self.tbldict["tbluspc"].objects.all().delete()
            self.tbldict["tblospc"].objects.all().delete()
            self.tbldict["tbluera"].objects.all().delete()
            self.tbldict["tbloera"].objects.all().delete()
            self.tbldict["tbluwnl"].objects.all().delete()
            self.tbldict["tblownl"].objects.all().delete()

            self.arr = list()
            self.params = presp()
        except:
            raise AppErr(
                {
                    "dayRec": dayRecFn(),
                    "errField": "dbloadiniStatus",
                    "errComment": "Ошибка в ini dbload",
                }
            )
        else:
            Dbsvcupd.objects.filter(yymmddUpd=dayRecFn()).update(dbloadiniStatus="OK")

    def exfn(self):

        sfn = Dbload()

        sfn.loadwln()
        sfn.loadfrt()
        sfn.loadgls()
        sfn.loadspc()
        sfn.loadera()
        sfn.loadwnl()

    def loadwln(self):
        try:
            odata = Conn11(self.params)
            self.arr = odata.conn()

            for ell in self.arr["users"]:

                r = self.tbldict["tbluwln"](
                    # nm=(str(ell['nm']).encode('utf-8', errors='ignore')).decode('utf-8'),
                    # nm=(str(ell['nm']).encode('unicode_escape')).decode('unicode_escape'),
                    # nm=ell['nm'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["nm"]),
                    uid=ell["id"],
                )
                r.save()

            for ell in self.arr["objects"]:
                r = self.tbldict["tblowln"](
                    # nm=(str(ell['nm']).encode('utf-8', errors='ignore')).decode('utf-8'),
                    # nm=(str(ell['nm']).encode('unicode_escape')).decode('unicode_escape'),
                    # nm=ell['nm'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["nm"]),
                    oid=ell["id"],
                    act=ell["act"],
                    crt=ell["crt"],
                    dactt=ell["dactt"],
                )
                r.save()
        except:
            raise AppErr(
                {
                    "dayRec": dayRecFn(),
                    "errField": "dbloadWlnStatus",
                    "errComment": "Ошибка в dbload при загрузке Wln",
                }
            )
        else:
            Dbsvcupd.objects.filter(yymmddUpd=dayRecFn()).update(dbloadWlnStatus="OK")

    def loadfrt(self):
        try:
            odata = Conn12(self.params)
            self.arr = odata.conn()

            for ell in self.arr["companies"]:
                # for k, ell in el.items():

                # print(ell)
                r = self.tbldict["tblufrt"](
                    # nm=ell['name'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["name"]),
                    uid=ell["id"],
                )
                r.save()

            for ell in self.arr["objects"]:
                r = self.tbldict["tblofrt"](
                    # nm=ell['name'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["name"]),
                    uid=ell["uid"],
                    oid=ell["id"],
                    gid=ell["groupId"],
                    # crt=ell['uid'],
                    imei=ell["IMEI"],
                )
                r.save()

            data = {"data": self.arr["companies"], "title": "Loaded"}
        except:
            raise AppErr(
                {
                    "dayRec": dayRecFn(),
                    "errField": "dbloadFrtStatus",
                    "errComment": "Ошибка в dbload при загрузке Frt",
                }
            )
        else:
            Dbsvcupd.objects.filter(yymmddUpd=dayRecFn()).update(dbloadFrtStatus="OK")

    def loadgls(self):
        try:
            odata = Conn13(self.params)
            self.arr = odata.conn()

            for ell in self.arr["companies"]:

                r = self.tbldict["tblugls"](
                    # nm=ell['name'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["name"]),
                    uid=ell["client"]["id"],
                )
                r.save()

            for ell in self.arr["objects"]:
                r = self.tbldict["tblogls"](
                    # nm=ell['nm'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["nm"]),
                    uid=ell["uid"],
                    oid=ell["oid"],
                    gid=ell["gid"],
                    # crt=ell['uid'],
                    imei=ell["imei"],
                )
                r.save()

            data = {"data": self.arr["companies"], "title": "Loaded"}
        except:
            raise AppErr(
                {
                    "dayRec": dayRecFn(),
                    "errField": "dbloadGlsStatus",
                    "errComment": "Ошибка в dbload при загрузке Gls",
                }
            )
        else:
            Dbsvcupd.objects.filter(yymmddUpd=dayRecFn()).update(dbloadGlsStatus="OK")

    def loadspc(self):
        try:
            odata = Conn14(self.params)
            self.arr = odata.conn()

            for ell in self.arr["objects"]:
                nmre = re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["Description"])
                rq = (
                    self.tbldict["tbluspc"]
                    .objects.all()
                    .filter(uid=(str(ell["CompanyId"]) + nmre))
                )
                if rq.count() == 0:
                    r = self.tbldict["tbluspc"](
                        # nm=ell['Description'],
                        nm=nmre,  # re.sub('[^0-9a-zA-ZА-я-_]+', ' ', ell['Description']),
                        uid=str(ell["CompanyId"]) + nmre,
                    )
                    r.save()

                r = self.tbldict["tblospc"](
                    # nm=ell['Name'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["Name"]),
                    uid=str(ell["CompanyId"]) + nmre,
                    oid=ell["UnitId"],
                    gid=ell["CompanyId"],
                    # crt=ell['uid'],
                    imei=ell["UnitId"],
                )
                r.save()

            data = {"data": self.arr["companies"], "title": "Loaded"}
        except:
            raise AppErr(
                {
                    "dayRec": dayRecFn(),
                    "errField": "dbloadSctStatus",
                    "errComment": "Ошибка в dbload при загрузке Sct",
                }
            )
        else:
            Dbsvcupd.objects.filter(yymmddUpd=dayRecFn()).update(dbloadSctStatus="OK")

    def loadera(self):
        try:
            odata = Conn15(self.params)
            self.arr = odata.conn()

            for ell in self.arr["objects"]:

                rq = self.tbldict["tbluera"].objects.all().filter(uid=ell["uid"])
                if rq.count() == 0:
                    r = self.tbldict["tbluera"](
                        # nm=ell['unm'],
                        nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["unm"]),
                        uid=ell["uid"],
                    )
                    r.save()

                r = self.tbldict["tbloera"](
                    # nm=ell['onm'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["onm"]),
                    uid=ell["uid"],
                    oid=ell["oid"],
                    gid=ell["uid"],
                    # crt=ell['uid'],
                    imei=ell["IMEI"],
                )
                r.save()

            data = {"data": self.arr["companies"], "title": "Loaded"}
        except:
            raise AppErr(
                {
                    "dayRec": dayRecFn(),
                    "errField": "dbloadEraStatus",
                    "errComment": "Ошибка в dbload при загрузке Era",
                }
            )
        else:
            Dbsvcupd.objects.filter(yymmddUpd=dayRecFn()).update(dbloadEraStatus="OK")

    def loadwnl(self):
        try:
            odata = Conn16(self.params)
            self.arr = odata.conn()

            for ell in self.arr["users"]:

                r = self.tbldict["tbluwnl"](
                    # nm=(str(ell['nm']).encode('utf-8', errors='ignore')).decode('utf-8'),
                    # nm=(str(ell['nm']).encode('unicode_escape')).decode('unicode_escape'),
                    # nm=ell['nm'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["nm"]),
                    uid=ell["id"],
                )
                r.save()

            for ell in self.arr["objects"]:
                r = self.tbldict["tblownl"](
                    # nm=(str(ell['nm']).encode('utf-8', errors='ignore')).decode('utf-8'),
                    # nm=(str(ell['nm']).encode('unicode_escape')).decode('unicode_escape'),
                    # nm=ell['nm'],
                    nm=re.sub("[^0-9a-zA-ZА-я-_]+", " ", ell["nm"]),
                    oid=ell["id"],
                    act=ell["act"],
                    crt=ell["crt"],
                    dactt=ell["dactt"],
                )
                r.save()
        except:
            raise AppErr(
                {
                    "dayRec": dayRecFn(),
                    "errField": "dbloadWlnStatus",
                    "errComment": "Ошибка в dbload при загрузке Wnl",
                }
            )
        else:
            Dbsvcupd.objects.filter(yymmddUpd=dayRecFn()).update(dbloadWlnStatus="OK")
