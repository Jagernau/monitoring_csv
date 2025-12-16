from sqlalchemy import BigInteger, CheckConstraint, Column, Date, DateTime, ForeignKey, Index, Integer, JSON, String, TIMESTAMP, Table, Text, Time, text
from sqlalchemy.dialects.mysql import DATETIME, LONGTEXT, SMALLINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata


class CellOperator(Base):
    __tablename__ = 'Cell_operator'
    __table_args__ = {'comment': 'Таблица для хранения информации об операторах сотовой связи'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(60), nullable=False, comment='Имя сотового оператора')
    ca_price = Column(Integer, comment='цена для клиентов')
    sun_price = Column(Integer, comment='Цена для Сантел')

    sim_cards = relationship('SimCards', back_populates='Cell_operator')


t_GOS_DUBLI = Table(
    'GOS_DUBLI', metadata,
    Column('gov_number', String(70)),
    Column('duplicate_count', BigInteger, server_default=text("'0'"))
)


t_ICCID_меньше_19 = Table(
    'ICCID меньше 19', metadata,
    Column('sim_iccid', String(40))
)


t_OKDESK_CONTACTS = Table(
    'OKDESK_CONTACTS', metadata,
    Column('change_time', TIMESTAMP, server_default=text('CURRENT_TIMESTAMP')),
    Column('ca_name', String(255)),
    Column('name', String(50)),
    Column('email', String(80))
)


class PPDKLogging(Base):
    __tablename__ = 'PPDK_logging'

    log_id = Column(Integer, primary_key=True, comment='Лог')
    column_name = Column(String(200, 'utf8mb3_unicode_ci'), nullable=False, comment='Название колонки')
    change_date = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Дата изменения')
    old_val = Column(String(700, 'utf8mb3_unicode_ci'), comment='Старое значение')
    new_val = Column(String(700, 'utf8mb3_unicode_ci'), comment='Новое значение')
    exist_id = Column(Integer, comment='OST_order_no')
    type_req = Column(String(100, 'utf8mb3_unicode_ci'), comment='Тип изменения')


class PPDKTransneft(Base):
    __tablename__ = 'PPDK_transneft'
    __table_args__ = {'comment': 'Заявки по ППДК транснефть'}

    id = Column(Integer, primary_key=True)
    OST_order_no = Column(Integer, nullable=False, comment='№ заявки в ОСТ\\r\\n')
    formation_date_app = Column(DateTime, nullable=False, comment='"Дата форми-\\r\\nрования заявки"\\r\\n')
    OST = Column(String(200, 'utf8mb3_unicode_ci'), nullable=False, comment='ОСТ\\r\\n')
    organization = Column(String(300, 'utf8mb3_unicode_ci'), nullable=False, comment='Организация\\r\\n')
    type_work = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='Вид работ\\r\\n')
    vehicle_reg_plate = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='"Регистра-\\r\\nционный знак ТС"\\r\\n')
    vehic_model = Column(String(300, 'utf8mb3_unicode_ci'), nullable=False, comment='Марка, модель ТС')
    comment = Column(VARCHAR(800), nullable=False, comment='Комментарий\\r\\n')
    date_first_initial = Column(DateTime, nullable=False, comment='"План. дата работ (перво-\\r\\nначальная предложенная заказчиком)"\\r\\n')
    plan_date_work = Column(DateTime, nullable=False, comment='План. дата работ (оконча-\\r\\nтельная)')
    vehic_invent_numb = Column(VARCHAR(200), comment='Инв. № ТС\\r\\n')
    vehicle_type = Column(String(200, 'utf8mb3_unicode_ci'), comment='Тип ТС\\r\\n')
    fault = Column(String(300, 'utf8mb3_unicode_ci'), comment='Неисправность\\r\\n')
    repair_area = Column(VARCHAR(700), comment='Площадка ремонта\\r\\n')
    date_transfer_MVDP = Column(DateTime, comment='Дата передачи в МВДП\\r\\n')
    date_agreement_contrac = Column(DateTime, comment='Дата согласования Исполнителем\\r\\n')
    processing_time = Column(DateTime, comment='Срок обработки\\r\\n')
    performer = Column(String(300, 'utf8mb3_unicode_ci'), comment='Исполнитель\\r\\n')
    date_centralized = Column(DateTime, comment='Дата и время Централизованной приемки работ\\r\\n')
    date_acceptance = Column(DateTime, comment='Дата и время приемки работ в ОСТ\\r\\n')
    dat_accept_works_OST = Column(DateTime, comment='Время приемки работ в ОСТ (в формате чч:мм)\\r\\n')
    status_req = Column(String(100, 'utf8mb3_unicode_ci'), comment='Статус\\r\\n')
    dat_closing_app = Column(DateTime, comment='Дата закрытия заявки\\r\\n')
    comment_primary_doc = Column(String(300, 'utf8mb3_unicode_ci'), comment='Комментарий, первичный документ из ППДК ОСТ\\r\\n')
    summary_act = Column(String(300, 'utf8mb3_unicode_ci'), comment='Сводный акт (в Модуле)\\r\\n')
    completion_date = Column(DateTime, comment='Дата завершения работ в ОСТ\\r\\n')
    days_overdue = Column(Integer, comment='Кол-во дней просрочки\\r\\n')


class AuthGroup(Base):
    __tablename__ = 'auth_group'
    __table_args__ = {'comment': 'Таблица для хранения групп пользователей ЦМС'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(150), nullable=False, unique=True, comment='Название группы пользователей ЦМС')

    auth_user_groups = relationship('AuthUserGroups', back_populates='group')
    auth_group_permissions = relationship('AuthGroupPermissions', back_populates='group')


class AuthUser(Base):
    __tablename__ = 'auth_user'
    __table_args__ = {'comment': 'Таблица пользователей ЦМС'}

    id = Column(Integer, primary_key=True)
    password = Column(VARCHAR(128), nullable=False, comment='пароль')
    is_superuser = Column(TINYINT(1), nullable=False, comment='принадлежность к суперпользователю')
    username = Column(VARCHAR(150), nullable=False, unique=True, comment='логин')
    first_name = Column(VARCHAR(150), nullable=False, comment='имя')
    last_name = Column(VARCHAR(150), nullable=False, comment='фамилия')
    email = Column(VARCHAR(254), nullable=False, comment='почта')
    is_staff = Column(TINYINT(1), nullable=False, comment='является ли сотрудником')
    is_active = Column(TINYINT(1), nullable=False, comment='активность аккаунта')
    date_joined = Column(DATETIME(fsp=6), nullable=False, comment='дата создания аккаунта')
    last_login = Column(DATETIME(fsp=6), comment='последний вход')

    auth_user_groups = relationship('AuthUserGroups', back_populates='user')
    devices_logger_commands = relationship('DevicesLoggerCommands', back_populates='auth_user')
    django_admin_log = relationship('DjangoAdminLog', back_populates='user')
    auth_user_user_permissions = relationship('AuthUserUserPermissions', back_populates='user')
    devices = relationship('Devices', back_populates='itprogrammer')
    devices_diagnostics = relationship('DevicesDiagnostics', back_populates='programmer')
    service_subscription_log = relationship('ServiceSubscriptionLog', back_populates='user')
    sim_cards = relationship('SimCards', back_populates='itprogrammer')


class DevicesVendor(Base):
    __tablename__ = 'devices_vendor'
    __table_args__ = {'comment': 'Таблица для хранения информации о производителях устройств'}

    id = Column(Integer, primary_key=True)
    vendor_name = Column(VARCHAR(35), comment='Название фирмы производителя терминалов')

    devices_brands = relationship('DevicesBrands', back_populates='devices_vendor')


class DiscountClient(Base):
    __tablename__ = 'discount_client'
    __table_args__ = {'comment': 'Таблица с вариантами скидок'}

    dis_cl_id = Column(Integer, primary_key=True, comment='ID Скидки')
    dis_cl_name = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='Название Скидки')
    dis_cl_rate = Column(Integer, nullable=False, comment='Процент')

    discount_client_link = relationship('DiscountClientLink', back_populates='dis')


class DiscountObj(Base):
    __tablename__ = 'discount_obj'
    __table_args__ = {'comment': 'Варианты скидок на объекты'}

    dis_obj_id = Column(Integer, primary_key=True, comment='ID скидки на объекты')
    dis_obj_name = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='Название скидок на объекты')
    dis_obj_rate = Column(Integer, nullable=False, comment='Процент скидки на объект')

    discount_obj_link = relationship('DiscountObjLink', back_populates='dis')


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        Index('django_content_type_app_label_model_76bd3d3b_uniq', 'app_label', 'model', unique=True),
        {'comment': 'Таблица для хранения типов содержимого Django ЦМС'}
    )

    id = Column(Integer, primary_key=True)
    app_label = Column(VARCHAR(100), nullable=False, comment='из какого приложения')
    model = Column(VARCHAR(100), nullable=False, comment='из какой модели')

    auth_permission = relationship('AuthPermission', back_populates='content_type')
    django_admin_log = relationship('DjangoAdminLog', back_populates='content_type')


class DjangoMigrations(Base):
    __tablename__ = 'django_migrations'
    __table_args__ = {'comment': 'Таблица для хранения информации о миграциях Django ЦМС'}

    id = Column(BigInteger, primary_key=True)
    app = Column(VARCHAR(255), nullable=False, comment='таблица')
    name = Column(VARCHAR(255), nullable=False, comment='действие')
    applied = Column(DATETIME(fsp=6), nullable=False, comment='дата')


class DjangoSession(Base):
    __tablename__ = 'django_session'
    __table_args__ = {'comment': 'Таблица для хранения сессий Django Заходов в ЦМС'}

    session_key = Column(String(40, 'utf8mb3_unicode_ci'), primary_key=True)
    session_data = Column(LONGTEXT, nullable=False)
    expire_date = Column(DATETIME(fsp=6), nullable=False, index=True)


class GlobalLogging(Base):
    __tablename__ = 'global_logging'
    __table_args__ = {'comment': 'Первоначальная Таблица для хранения изменений в таблицах объектов '
                'и клиентов 1с через Python, до тригерного логирования'}

    id = Column(Integer, primary_key=True)
    section_type = Column(VARCHAR(50), nullable=False, comment='изменения в объектах или клиентах')
    edit_id = Column(Integer, nullable=False, comment='id изменённого')
    field = Column(VARCHAR(50), nullable=False, comment='поле изменения')
    old_value = Column(VARCHAR(8000), comment='старое значение')
    new_value = Column(VARCHAR(8000), comment='новое значение')
    change_time = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    sys_id = Column(Integer, comment='Система мониторинга')
    action = Column(VARCHAR(100), comment='добавление, изменение или удаление')
    contragent_id = Column(Integer, comment='логгирование контрагента')


class GuaranteeTerms(Base):
    __tablename__ = 'guarantee_terms'
    __table_args__ = {'comment': 'Таблица для хранения родителей контрагентов'}

    gt_id = Column(Integer, primary_key=True, comment='ID гарантийного срока')
    gt_term = Column(Integer, comment='Срок гарантии (дней)')
    gt_type = Column(VARCHAR(255), comment='Тип гарантии')


class Holdings(Base):
    __tablename__ = 'holdings'
    __table_args__ = {'comment': 'Таблица для хранения информации о Холдингах по тз'}

    holding_id = Column(Integer, primary_key=True)
    holding_name = Column(VARCHAR(255), comment='Имя родителя контрагента (Холдинг)')

    Contragents = relationship('Contragents', back_populates='ca_holding')


class InfoServTarifClient(Base):
    __tablename__ = 'info_serv_tarif_client'
    __table_args__ = {'comment': 'Сопоставление ТАРИФ СЕРВИСОВ КЛИЕНТ'}

    tarif_client_id = Column(Integer, primary_key=True, comment='ИД отношений')
    tarif_id = Column(Integer, nullable=False, index=True, comment='ID Тарифа')
    client_id = Column(Integer, nullable=False, index=True, comment='ID Клиента')
    start_tarif = Column(Date, comment='Начало тарифа у клиента')
    end_tarif = Column(Date, comment='Конец тарифа')


class InfoServTarifs(Base):
    __tablename__ = 'info_serv_tarifs'
    __table_args__ = {'comment': 'Таблица с ТАРИФАМИ СЕРВИСОВ'}

    tarif_id = Column(Integer, primary_key=True, comment='ИД тарифов')
    name = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='Название тарифа')
    price = Column(Integer, nullable=False, comment='Цена тарифа')
    count = Column(Integer, comment='Количество доступных сервисов')


class InformationServices(Base):
    __tablename__ = 'information_services'
    __table_args__ = {'comment': 'Таблица для информационных сервисов Клиентов'}

    serv_id = Column(Integer, primary_key=True, comment='ID Сервиса')
    serv_name = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, unique=True, comment='Название сервиса')
    serv_price = Column(Integer, comment='Цена за сервис')

    info_serv_obj = relationship('InfoServObj', back_populates='info_obj_serv')


class LogChanges(Base):
    __tablename__ = 'log_changes'
    __table_args__ = {'comment': 'Таблица логирования изменений в данных Базы'}

    log_id = Column(Integer, primary_key=True)
    changes_date = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), comment='Дата изменения')
    changes_table = Column(VARCHAR(250), comment='В какой таблице были внесены изменения')
    changes_action = Column(TINYINT, comment='Название действия:\\r\\n0 - Del\\r\\n1 - Insert\\r\\n2 - Update')
    obj_key = Column(Integer, comment='Ключ элемента, Практически везде ID. Делаю по ID int')
    changes_column = Column(VARCHAR(255), comment='Название столбца')
    old_val = Column(VARCHAR(255), comment='Старое значение')
    new_val = Column(VARCHAR(255), comment='Новое значение')


class LoginUsersPhones(Base):
    __tablename__ = 'login_users_phones'
    __table_args__ = {'comment': 'Таблица с логинами и паролями и телефонами'}

    id = Column(Integer, primary_key=True, comment='ID записи')
    phone = Column(String(12, 'utf8mb3_unicode_ci'), nullable=False, comment='телефон')
    login = Column(String(12, 'utf8mb3_unicode_ci'), nullable=False, comment='Логин')
    password = Column(String(19, 'utf8mb3_unicode_ci'), nullable=False, comment='Пароль')
    mess_name = Column(String(40, 'utf8mb3_unicode_ci'), nullable=False, comment='Имя в месседжере')
    mess_user_id = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='ID в меседжере')


class MonitoringSystem(Base):
    __tablename__ = 'monitoring_system'
    __table_args__ = {'comment': 'Таблица для хранения информации о системах мониторинга'}

    mon_sys_id = Column(Integer, primary_key=True)
    mon_sys_name = Column(VARCHAR(60), comment='Название системы мониторинга')
    mon_sys_obj_price_suntel = Column(Integer, comment='Стоимость объекта для Сантел')
    mon_sys_ca_obj_price_default = Column(Integer, comment='Базовая стоимость объекта для Контрагента')
    mon_url = Column(String(200, 'utf8mb3_unicode_ci'), comment='Адресс Системы мониторинга')

    inspect_terminals = relationship('InspectTerminals', back_populates='monitoring_system_')
    invoicing = relationship('Invoicing', back_populates='system_monitorig')
    Login_users = relationship('LoginUsers', back_populates='system')
    ca_objects = relationship('CaObjects', back_populates='sys_mon')
    clients_in_system_monitor = relationship('ClientsInSystemMonitor', back_populates='system_monitor')
    devices = relationship('Devices', back_populates='sys_mon')
    info_serv_obj = relationship('InfoServObj', back_populates='monitoring_system')
    billing = relationship('Billing', back_populates='sys_mon')


class ObjectRetranslators(Base):
    __tablename__ = 'object_retranslators'
    __table_args__ = {'comment': 'Таблица для хранения информации о ретрансляторах'}

    retranslator_id = Column(Integer, primary_key=True)
    retrans_protocol = Column(TINYINT, nullable=False, comment='Виды протоколов:\\r\\n1- Egts\\r\\n2 - Wialon ретранслятор\\r\\n3- Wialon IPS')
    retranslator_name = Column(VARCHAR(50), comment='Имя ретранслятора')
    retranslator_suntel_price = Column(Integer, comment='цена ретрансляции для Сантел')
    retranslator_ca_price = Column(Integer, comment='Цена ретрансляции для клиента')
    retrans_adres = Column(String(200, 'utf8mb3_unicode_ci'), comment='Адрес куда ретранслируется')

    group_object_retrans = relationship('GroupObjectRetrans', back_populates='retr')
    billing = relationship('Billing', back_populates='retrans')


class ObjectStatuses(Base):
    __tablename__ = 'object_statuses'
    __table_args__ = {'comment': 'Таблица для хранения информации о статусах объектов'}

    status_id = Column(Integer, primary_key=True)
    abon_bool = Column(TINYINT(1), nullable=False, comment='На абонентке или нет')
    status = Column(VARCHAR(50), comment='Название статуса')

    ca_objects = relationship('CaObjects', back_populates='object_statuses')
    billing = relationship('Billing', back_populates='obj_status')


class OkDeskLoggingIss(Base):
    __tablename__ = 'ok_desk_logging_iss'
    __table_args__ = {'comment': 'Логгирование изменение в заявках ОКДЕСК'}

    id = Column(Integer, primary_key=True)
    section_type = Column(String(100, 'utf8mb3_unicode_ci'), comment='изменения в объектах или клиентах')
    edit_id = Column(Integer, comment='id изменённого')
    field = Column(String(100, 'utf8mb3_unicode_ci'), comment='поле изменения')
    old_value = Column(JSON, comment='старое значение')
    new_value = Column(JSON, comment='новое значение')
    change_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), comment='Время создания заявки')
    action = Column(String(100, 'utf8mb3_unicode_ci'), comment='добавление, изменение или удаление\t')


class OnecContacts(Base):
    __tablename__ = 'onec_contacts'
    __table_args__ = {'comment': 'Контакты'}

    contact_id = Column(Integer, primary_key=True, comment='Идентификатор Контактов')
    usesokdesk = Column(TINYINT, nullable=False, comment='ИспользуетOKDESK\\r\\nИспользуется Ли в ОКДЕСК\\r\\n0-НЕТ\\r\\n1_ДА')
    connectedtelegram_bot = Column(TINYINT, nullable=False, comment='ПодключенКТелеграм_Боту\\r\\nПодключённ ли к телеграмм\\r\\n0-нет\\r\\n1-Да')
    connectedcmob_application = Column(TINYINT, nullable=False, comment='ПодключенКМоб_Приложению\\r\\n0-нет\\r\\n1-да')
    access_personal_okdesk = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='Предоставлен ли доступ клиенту к ОКДЕСК')
    surname = Column(String(50, 'utf8mb3_unicode_ci'), comment='Фамилия')
    name = Column(String(50, 'utf8mb3_unicode_ci'), comment='Имя')
    patronymic = Column(String(50, 'utf8mb3_unicode_ci'), comment='Отчество')
    position = Column(String(100, 'utf8mb3_unicode_ci'), comment='Должность')
    phone = Column(String(80, 'utf8mb3_unicode_ci'), comment='Телефон')
    mobiletelephone = Column(String(80, 'utf8mb3_unicode_ci'), comment='МобТелефон')
    email = Column(String(80, 'utf8mb3_unicode_ci'), comment='ЭлПочта')
    unique_partner_identifier = Column(String(200, 'utf8mb3_unicode_ci'), comment='УникальныйИдентификаторПартнера')
    unique_contact_identifier = Column(String(200, 'utf8mb3_unicode_ci'), comment='УникальныйИдентификаторКонтактногоЛица')
    ok_desk_id = Column(Integer, comment='ИД в ОК ДЕСК')
    nametelegram = Column(VARCHAR(200), comment='ИмяВТелеграм')
    idbmob_application = Column(VARCHAR(200), comment='IDВМоб_Приложении')


class OnecContracts(Base):
    __tablename__ = 'onec_contracts'
    __table_args__ = {'comment': 'Таблица с договорами из 1С'}

    contract_id = Column(Integer, primary_key=True, comment='Внутренний ID контракта')
    unique_contract_identifier = Column(String(200, 'utf8mb3_unicode_ci'), nullable=False, comment='УникальныйИдентификаторДоговораКонтрагента')
    name_contract = Column(String(100, 'utf8mb3_unicode_ci'), comment='НаименованиеДоговора')
    contract_number = Column(String(100, 'utf8mb3_unicode_ci'), comment='НомерДоговора')
    contract_date = Column(Date, comment='ДатаДоговора')
    contract_status = Column(VARCHAR(50), comment='Статус')
    organization = Column(String(200, 'utf8mb3_unicode_ci'), comment='Организация')
    partner = Column(VARCHAR(1000), comment='Партнер')
    counterparty = Column(String(1000, 'utf8mb3_unicode_ci'), comment='Контрагент')
    contract_commencement_date = Column(Date, comment='ДатаНачалаДействия')
    contract_expiration_date = Column(Date, comment='ДатаОкончанияДействия')
    contract_purpose = Column(String(200, 'utf8mb3_unicode_ci'), comment='Цель')
    type_calculations = Column(String(200, 'utf8mb3_unicode_ci'), comment='ВидРасчетов')
    category = Column(String(100, 'utf8mb3_unicode_ci'), comment='Категория')
    manager = Column(String(200, 'utf8mb3_unicode_ci'), comment='Менеджер')
    subdivision = Column(String(600, 'utf8mb3_unicode_ci'), comment='Подразделение')
    contact_person = Column(String(300, 'utf8mb3_unicode_ci'), comment='КонтактноеЛицо')
    organization_bank_account = Column(String(300, 'utf8mb3_unicode_ci'), comment='БанковскийСчетОрганизации')
    counterparty_bank_account = Column(String(300, 'utf8mb3_unicode_ci'), comment='БанковскийСчетКонтрагента')
    detailed_calculations = Column(String(200, 'utf8mb3_unicode_ci'), comment='ДетализацияРасчетов')
    unique_partner_identifier = Column(String(500, 'utf8mb3_unicode_ci'), comment='УникальныйИдентификаторПартнера')
    unique_counterparty_identifier = Column(String(500, 'utf8mb3_unicode_ci'), comment='УникальныйИдентификаторКонтрагента')
    ok_desk_id = Column(Integer, comment='ID в ОК-деск')
    signing_status = Column(String(100, 'utf8mb3_unicode_ci'), comment='СтатусПодписания')


class OnecOrder(Base):
    __tablename__ = 'onec_order'
    __table_args__ = {'comment': 'Таблица заказ нарядов из 1С'}

    order_id = Column(Integer, primary_key=True)
    order_unic_id = Column(String(50, 'utf8mb3_unicode_ci'), nullable=False, comment='УникальныйИдентификаторАктаТО')
    order_num = Column(String(50, 'utf8mb3_unicode_ci'), nullable=False, comment='ЗаказНарядНомер')
    order_data = Column(DateTime, nullable=False, comment='Дата')
    edit_date = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Время создания записи')


class RequestsFromOKDESK(Base):
    __tablename__ = 'requests_from_OKDESK'

    db_id = Column(Integer, primary_key=True, comment='Внутренний ИД')
    ok_desk_id = Column(Integer, nullable=False, unique=True, comment='ИД заявки в ОКДЕСК')
    req_data_db = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Время создания записи в БД')
    title = Column(String(300, 'utf8mb3_unicode_ci'), comment='Название заявки')
    created_at = Column(DateTime, comment='Дата создания')
    completed_at = Column(DateTime, comment='Закончена')
    deadline_at = Column(DateTime, comment='Конечный срок')
    delay_to = Column(DateTime, comment='Продлена до')
    planned_reaction_a = Column(DateTime, comment='Плановая дата реакции')
    reacted_at = Column(DateTime, comment='Время реакции')
    without_answer = Column(TINYINT, comment='Без ответа')
    updated_at = Column(DateTime, comment='Обновлено')
    status = Column(JSON, comment='Статус заявки')
    type_req = Column(JSON, comment='Тип заявки')
    priority = Column(JSON, comment='Приоритет заявки')
    company = Column(JSON, comment='Компания на ком заявка')
    contact = Column(JSON, comment='Контакт')
    service_object = Column(JSON, comment='Объект')
    agreement = Column(JSON, comment='договор')
    equipments = Column(JSON, comment='Оборудование')
    comments = Column(JSON, comment='Коментарии')
    specifications = Column(JSON, comment='Спецификации Заявки')
    observers = Column(JSON, comment='Наблюдатели')
    assignee = Column(JSON, comment='Исполнители')
    parameters = Column(JSON, comment='Параметры заявки')


class SensorVendor(Base):
    __tablename__ = 'sensor_vendor'
    __table_args__ = {'comment': 'Производители датчиков'}

    id = Column(Integer, primary_key=True, comment='ID изготовителя Датчиков')
    name = Column(String(200, 'utf8mb3_unicode_ci'), nullable=False, comment='Имя производителя')

    sensor_brands = relationship('SensorBrands', back_populates='sensor_vendor')


class UserLogging(Base):
    __tablename__ = 'user_logging'
    __table_args__ = {'comment': 'Таблица для хранения логов действий пользователей Базы данных, '
                'например пользователя Битрикс или Разработчиков Махалова'}

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50, 'utf8mb3_unicode_ci'))
    action_type = Column(String(50, 'utf8mb3_unicode_ci'))
    action_date = Column(Date)
    action_time = Column(Time)
    old_val = Column(Text(collation='utf8mb3_unicode_ci'))
    new_val = Column(String(300, 'utf8mb3_unicode_ci'))
    action_description = Column(TEXT)


t_Вытягивание_госНомеров_по_типу_А123АБ12 = Table(
    'Вытягивание госНомеров по типу А123АБ12', metadata,
    Column('object_name', String(70)),
    Column('contragent_id', Integer)
)


t_Дубли_ICCID_по_маске_19_символов = Table(
    'Дубли ICCID по маске 19 символов', metadata,
    Column('sim_iccid', String(19)),
    Column('count', BigInteger, server_default=text("'0'"))
)


t_Дубли_номеров = Table(
    'Дубли номеров', metadata,
    Column('gn', String(25)),
    Column('ct', BigInteger, server_default=text("'0'"))
)


t_Не_привязанные_Объекты_к_КЛиентам = Table(
    'Не привязанные Объекты к КЛиентам', metadata,
    Column('mon_sys_name', String(60)),
    Column('object_name', String(70)),
    Column('owner_contragent', String(200)),
    Column('owner_user', String(255))
)


t_Одинаковые_инн = Table(
    'Одинаковые инн', metadata,
    Column('ca_inn', String(60)),
    Column('count', BigInteger, server_default=text("'0'"))
)


t_Одинаковые_логины = Table(
    'Одинаковые логины', metadata,
    Column('login', String(60)),
    Column('count', BigInteger, server_default=text("'0'"))
)


t_Сим_1378___Терминал_4752 = Table(
    'Сим 1378 - Терминал 4752', metadata,
    Column('device_serial', String(100)),
    Column('device_imei', String(60)),
    Column('terminal_date', DateTime),
    Column('name', String(200)),
    Column('ca_name', String(255)),
    Column('sim_iccid', String(40)),
    Column('sim_tel_number', String(40))
)


class Contragents(Base):
    __tablename__ = 'Contragents'
    __table_args__ = {'comment': 'Таблица для хранения информации о контрагентах по тз'}

    ca_id = Column(Integer, primary_key=True)
    ca_holding_id = Column(ForeignKey('holdings.holding_id'), index=True, comment='ID холдинга')
    ca_name = Column(VARCHAR(255), comment='НаименованиеПартнёра')
    ca_shortname = Column(VARCHAR(250), comment='НаименованиеПолноеПартнёра')
    ca_inn = Column(VARCHAR(60), comment='ИНН')
    ca_kpp = Column(VARCHAR(60), comment='КПП')
    ca_bill_account_num = Column(VARCHAR(60), comment='Расчетный счет ????????')
    ca_bill_account_bank_name = Column(VARCHAR(60), comment='Наименование банка ????')
    ca_bill_account_ogrn = Column(VARCHAR(60), comment='ОГРН ????????')
    ca_edo_connect = Column(TINYINT(1), comment='Обмен ЭДО ??????')
    ca_field_of_activity = Column(VARCHAR(260), comment='НаправлениеБизнесаКонтрагента')
    ca_type = Column(VARCHAR(60), comment='ЮрФизЛицоПартёр')
    unique_onec_id = Column(VARCHAR(100), comment='УникальныйИдентификаторПарнёра')
    registration_date = Column(Date, comment='Дата регистрации в 1С')
    key_manager = Column(VARCHAR(200), comment='Основной менеджер ')
    actual_address = Column(VARCHAR(300), comment='Фактический адрес ')
    registered_office = Column(VARCHAR(300), comment='Юридический адрес ')
    phone = Column(VARCHAR(200), comment='Телефон ')
    ca_uid_contragent = Column(String(100, 'utf8mb3_unicode_ci'), comment='УникальныйИдентификаторКонтрагента')
    ca_name_contragent = Column(String(255, 'utf8mb3_unicode_ci'), comment='НаименованиеКонтрагента')
    service_manager = Column(String(100, 'utf8mb3_unicode_ci'), comment='Имя прикреплённого менеджера тех поддержки')
    ok_desk_id = Column(Integer, comment='id в ОК деске')
    ca_tarif = Column(VARCHAR(20), comment='Тариф Клиента')

    ca_holding = relationship('Holdings', back_populates='Contragents')
    Login_users = relationship('LoginUsers', back_populates='contragent')
    ca_contacts = relationship('CaContacts', back_populates='ca')
    ca_contracts = relationship('CaContracts', back_populates='ca')
    ca_objects = relationship('CaObjects', back_populates='contragent')
    clients_in_system_monitor = relationship('ClientsInSystemMonitor', back_populates='client')
    devices = relationship('Devices', back_populates='contragent')
    discount_client_link = relationship('DiscountClientLink', back_populates='cl')
    equipment_warehouse = relationship('EquipmentWarehouse', back_populates='client')
    object_sensors = relationship('ObjectSensors', back_populates='client')
    sender_logger = relationship('SenderLogger', back_populates='send_client')
    object_vehicles = relationship('ObjectVehicles', back_populates='vehicle_ca')
    sim_cards = relationship('SimCards', back_populates='contragent')
    billing = relationship('Billing', back_populates='client')


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        Index('auth_permission_content_type_id_codename_01ab375a_uniq', 'content_type_id', 'codename', unique=True),
        {'comment': 'Таблица разрешений для пользователей ЦМС'}
    )

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False, comment='Название разрешения для пользователя ЦМС')
    content_type_id = Column(ForeignKey('django_content_type.id'), nullable=False, comment='Возможность выполнять действия в ЦМС')
    codename = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False)

    content_type = relationship('DjangoContentType', back_populates='auth_permission')
    auth_group_permissions = relationship('AuthGroupPermissions', back_populates='permission')
    auth_user_user_permissions = relationship('AuthUserUserPermissions', back_populates='permission')


class AuthUserGroups(Base):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        Index('auth_user_groups_user_id_group_id_94350c0c_uniq', 'user_id', 'group_id', unique=True),
        {'comment': 'Таблица связи пользователей с группами в системе аутентификации '
                'ЦМС'}
    )

    id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False, comment='связь с пользователем ЦМС')
    group_id = Column(ForeignKey('auth_group.id'), nullable=False, index=True, comment='связь с группой пользователей ЦМС')

    group = relationship('AuthGroup', back_populates='auth_user_groups')
    user = relationship('AuthUser', back_populates='auth_user_groups')


class DevicesBrands(Base):
    __tablename__ = 'devices_brands'
    __table_args__ = {'comment': 'Таблица для хранения информации о моделях устройств'}

    id = Column(Integer, primary_key=True)
    name = Column(String(200, 'utf8mb3_unicode_ci'))
    devices_vendor_id = Column(ForeignKey('devices_vendor.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Id Вендора терминалов')

    devices_vendor = relationship('DevicesVendor', back_populates='devices_brands')
    devices = relationship('Devices', back_populates='devices_brand')
    devices_commands = relationship('DevicesCommands', back_populates='devices_brands')
    equipment_warehouse = relationship('EquipmentWarehouse', back_populates='terminal_model')


class DevicesLoggerCommands(Base):
    __tablename__ = 'devices_logger_commands'
    __table_args__ = {'comment': 'Таблица для хранения журнала команд, отправленных на устройства '
                'через ЦМС не по ТЗ'}

    id = Column(Integer, primary_key=True)
    command_date = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Время отправки команды ')
    command_resresponse = Column(VARCHAR(200), nullable=False, comment='Ответ на команду')
    command_send = Column(VARCHAR(200), nullable=False, comment='Команда')
    programmer = Column(ForeignKey('auth_user.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Кто отправил команду')
    terminal_imei = Column(String(50, 'utf8mb3_unicode_ci'), nullable=False, comment='imei терминала')

    auth_user = relationship('AuthUser', back_populates='devices_logger_commands')


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'
    __table_args__ = (
        CheckConstraint('(`action_flag` >= 0)'),
        {'comment': 'Таблица для хранения журнала действий администратора ЦМС'}
    )

    id = Column(Integer, primary_key=True)
    action_time = Column(DATETIME(fsp=6), nullable=False, comment='Время операции')
    object_repr = Column(VARCHAR(200), nullable=False, comment='что было изменено')
    action_flag = Column(SMALLINT, nullable=False, comment='какое действие было выполнено')
    change_message = Column(LONGTEXT, nullable=False, comment='на что изменено')
    user_id = Column(ForeignKey('auth_user.id'), nullable=False, index=True, comment='кто из пользователей ЦМС внёс изменения')
    object_id = Column(LONGTEXT, comment='id объекта Бд было произведено действие')
    content_type_id = Column(ForeignKey('django_content_type.id'), index=True, comment='в какой таблице были изменения')

    content_type = relationship('DjangoContentType', back_populates='django_admin_log')
    user = relationship('AuthUser', back_populates='django_admin_log')


class InspectTerminals(Base):
    __tablename__ = 'inspect_terminals'
    __table_args__ = {'comment': 'Таблица по обходу терминалов'}

    inspect_id = Column(Integer, primary_key=True, comment='ID Инспекции')
    inspect_date = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Времяинспекции')
    type_term = Column(VARCHAR(50), comment='Тип терминала')
    imei = Column(String(100, 'utf8mb3_unicode_ci'), comment='IMEIТерминала')
    iccid = Column(VARCHAR(100), comment='ICCID СИМкарты')
    vehicleId = Column(String(50, 'utf8mb3_unicode_ci'), comment='ID Как в СМ')
    vehicle_name = Column(String(50, 'utf8mb3_unicode_ci'), comment='Имя Объекта')
    client_name = Column(String(400, 'utf8mb3_unicode_ci'), comment='Имя клиента как в 1С')
    client_id = Column(Integer, comment='ИД клиента из клиентов БД')
    iccid_in_db = Column(Integer, comment='Наличие Сим карты в нашей БД\\r\\n0-Клментская сим\\r\\n1-наша')
    if_change_imei = Column(Integer, comment='Будет ли изменён IMEI у сим\\r\\n0-нет\\r\\n1-да')
    old_sim_imei = Column(String(100, 'utf8mb3_unicode_ci'), comment='Если не сходится IMEI в СИМ заносится сюда ')
    monitoring_system = Column(ForeignKey('monitoring_system.mon_sys_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Система Мониторинга')

    monitoring_system_ = relationship('MonitoringSystem', back_populates='inspect_terminals')


class Invoicing(Base):
    __tablename__ = 'invoicing'
    __table_args__ = {'comment': 'Таблица для хранения информации о счетах-фактурах по объекту '
                'вытащенный из другой БД postgres'}

    invoic_id = Column(Integer, primary_key=True)
    system_monitorig_id = Column(ForeignKey('monitoring_system.mon_sys_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Связь к системе мониторинга из ПУКС')
    system_object_id = Column(String(200, 'utf8mb3_unicode_ci'), nullable=False, comment='ID в системе мониторинга из ПУКС')
    add_time = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='дата')
    puks_tarif = Column(Integer, comment='Тариф из ПУКС')

    system_monitorig = relationship('MonitoringSystem', back_populates='invoicing')


class SensorBrands(Base):
    __tablename__ = 'sensor_brands'
    __table_args__ = {'comment': 'Таблица моделей датчиков'}

    id = Column(Integer, primary_key=True, comment='ID Модели')
    name = Column(String(200, 'utf8mb3_unicode_ci'), nullable=False, comment='Название модели')
    sensor_vendor_id = Column(ForeignKey('sensor_vendor.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Связь к Фирме изготовителя')
    model_type = Column(TINYINT, comment='Тип датчика: \\r\\n1 ДУТ.\\r\\n2 Температуры.\\r\\n3 Наклона.\\r\\n4 Индикатор.')

    sensor_vendor = relationship('SensorVendor', back_populates='sensor_brands')
    equipment_warehouse = relationship('EquipmentWarehouse', back_populates='sensor')
    object_sensors = relationship('ObjectSensors', back_populates='sensor_model')


class LoginUsers(Base):
    __tablename__ = 'Login_users'
    __table_args__ = {'comment': 'Таблица для хранения информации о пользователях систем '
                'мониторинга'}

    id = Column(Integer, primary_key=True)
    account_status = Column(TINYINT, nullable=False, server_default=text("'1'"), comment='Состояние учётки 0-остановлена, 1-не подтверждена но активна, 2-подтверждена и активна 3 -тестовая\\r\\n4- Учётка для учёта ТС\\r\\n\\r\\n')
    client_name = Column(VARCHAR(200), comment='Старая колонка, при ведении excel таблицы')
    login = Column(VARCHAR(60), comment='логин')
    email = Column(VARCHAR(60), comment='почта')
    password = Column(VARCHAR(60), comment='пароль')
    date_create = Column(Date, comment='дата создания')
    system_id = Column(ForeignKey('monitoring_system.mon_sys_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Ключ к системе мониторинга')
    contragent_id = Column(ForeignKey('Contragents.ca_id', ondelete='SET NULL', onupdate='RESTRICT'), index=True, comment='ID контрагента')
    comment_field = Column(String(270, 'utf8mb3_unicode_ci'), comment='Поле с комментариями')
    ca_uid = Column(VARCHAR(100), comment='Уникальный id контрагента')

    contragent = relationship('Contragents', back_populates='Login_users')
    system = relationship('MonitoringSystem', back_populates='Login_users')
    is_billing = Column(TINYINT, comment='Билинговый признак')


class AuthGroupPermissions(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        Index('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'group_id', 'permission_id', unique=True),
        {'comment': 'Таблица связи групп пользователей ЦМС с разрешениями'}
    )

    id = Column(BigInteger, primary_key=True)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False, comment='Связь с группой пользователей ЦМС')
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True, comment='Связь с разрешениями действий в ЦМС')

    group = relationship('AuthGroup', back_populates='auth_group_permissions')
    permission = relationship('AuthPermission', back_populates='auth_group_permissions')


class AuthUserUserPermissions(Base):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        Index('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq', 'user_id', 'permission_id', unique=True),
        {'comment': 'Таблица связи пользователей с разрешениями в системе '
                'аутентификации ЦМС'}
    )

    id = Column(BigInteger, primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    permission = relationship('AuthPermission', back_populates='auth_user_user_permissions')
    user = relationship('AuthUser', back_populates='auth_user_user_permissions')


class CaContacts(Base):
    __tablename__ = 'ca_contacts'
    __table_args__ = {'comment': 'Таблица для хранения контактной информации Клиентов по тз'}

    ca_contact_id = Column(Integer, primary_key=True)
    ca_id = Column(ForeignKey('Contragents.ca_id'), index=True, comment='связь с id компании')
    ca_contact_name = Column(VARCHAR(255), comment='Имя контактного лица')
    ca_contact_surname = Column(VARCHAR(255), comment='Фамилия контактного лица')
    ca_contact_middlename = Column(VARCHAR(255), comment='Отчество контактного лица')
    ca_contact_cell_num = Column(VARCHAR(255), unique=True, comment='Сотовый телефон контакт. лица')
    ca_contact_work_num = Column(VARCHAR(255), comment='Рабочий телефон к.л.')
    ca_contact_email = Column(VARCHAR(255), comment='Электр.почт. к.л')
    ca_contact_position = Column(VARCHAR(255), comment='Должность к.л.')

    ca = relationship('Contragents', back_populates='ca_contacts')


class CaContracts(Base):
    __tablename__ = 'ca_contracts'
    __table_args__ = {'comment': 'Таблица для хранения информации о контрактах по тз'}

    contract_id = Column(Integer, primary_key=True)
    ca_id = Column(ForeignKey('Contragents.ca_id'), index=True, comment='ID контрагента')
    contract_type = Column(VARCHAR(50), comment='Тип договора\\r\\nя бы сделал choice')
    contract_num_prefix = Column(VARCHAR(50), comment='Префикс номера договора')
    contract_num = Column(VARCHAR(50), comment='Номер договора')
    contract_payment_term = Column(VARCHAR(50), comment='условия оплаты')
    contract_payment_period = Column(VARCHAR(50), comment='Период оплаты')
    contract_start_date = Column(Date, comment='Дата заключения договора')
    contract_expired_date = Column(Date, comment='Дата завершения договора')

    ca = relationship('Contragents', back_populates='ca_contracts')


class CaObjects(Base):
    __tablename__ = 'ca_objects'
    __table_args__ = {'comment': 'Таблица для хранения информации об объектах из систем мониторинга'}

    id = Column(Integer, primary_key=True)
    sys_mon_id = Column(ForeignKey('monitoring_system.mon_sys_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ID системы мониторинга')
    sys_mon_object_id = Column(VARCHAR(50), comment='ID объекта в системе мониторинга. Единственное за что можно зацепиться')
    object_name = Column(VARCHAR(70), comment='Название объекта')
    object_status = Column(ForeignKey('object_statuses.status_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Статус объекта ссылается к статусам')
    object_add_date = Column(DateTime, comment='Дата добавления объекта')
    object_last_message = Column(DateTime, comment='Дата последнего сообщения')
    object_margin = Column(Integer, comment='Надбавка к базовой цене объекта')
    owner_contragent = Column(VARCHAR(200), comment='Хозяин контрагент, как в системе мониторинга.')
    owner_user = Column(VARCHAR(255), comment='Хозяин юзер. Логин пользователя в системе мониторинга')
    imei = Column(VARCHAR(100), comment='идентификатор терминала')
    updated = Column(DateTime, comment='Когда изменён')
    object_created = Column(DateTime, comment='Дата создания в системе мониторинга ')
    parent_id_sys = Column(VARCHAR(200), comment='Id клиента в системе мониторинга')
    contragent_id = Column(ForeignKey('Contragents.ca_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    ca_uid = Column(String(100, 'utf8mb3_unicode_ci'), comment='Уникальный id контрагента')
    ok_desk_id = Column(Integer, comment='ID объекта в ОК-деске')

    contragent = relationship('Contragents', back_populates='ca_objects')
    object_statuses = relationship('ObjectStatuses', back_populates='ca_objects')
    sys_mon = relationship('MonitoringSystem', back_populates='ca_objects')
    discount_obj_link = relationship('DiscountObjLink', back_populates='obj')
    group_object_retrans = relationship('GroupObjectRetrans', back_populates='obj')
    info_serv_obj = relationship('InfoServObj', back_populates='serv_obj_sys_mon')
    object_vehicles = relationship('ObjectVehicles', back_populates='vehicle_object')
    service_subscription_log = relationship('ServiceSubscriptionLog', back_populates='object')
    billing = relationship('Billing', back_populates='obj')


class ClientsInSystemMonitor(Base):
    __tablename__ = 'clients_in_system_monitor'
    __table_args__ = {'comment': 'Таблица для хранения информации об id клиентов и id родителей '
                'клиентов в СМ не по ТЗ'}

    id = Column(Integer, primary_key=True)
    id_in_system_monitor = Column(VARCHAR(200), comment='Id клиента в системе мониторинга')
    name_in_system_monitor = Column(VARCHAR(200), comment='Имя клиента в системе мониторинга ')
    owner_id_sys_mon = Column(VARCHAR(200), comment='Id хозяина в системе мониторинга')
    system_monitor_id = Column(ForeignKey('monitoring_system.mon_sys_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Id системы мониторинга ')
    client_id = Column(ForeignKey('Contragents.ca_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='id клиента')

    client = relationship('Contragents', back_populates='clients_in_system_monitor')
    system_monitor = relationship('MonitoringSystem', back_populates='clients_in_system_monitor')


class Devices(Base):
    __tablename__ = 'devices'
    __table_args__ = {'comment': 'Таблица для хранения информации об устройствах '
                'запрограммированных IT отделом не по тз'}

    device_id = Column(Integer, primary_key=True)
    device_serial = Column(VARCHAR(100), nullable=False, unique=True, comment='Серийный номер устройства')
    device_imei = Column(VARCHAR(60), unique=True, comment='IMEI устройства')
    client_name = Column(String(300, 'utf8mb3_unicode_ci'), comment='Имя клиента')
    terminal_date = Column(DateTime, comment='Дата программирования терминала')
    devices_brand_id = Column(ForeignKey('devices_brands.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ID Модели устройства ')
    name_it = Column(VARCHAR(50), comment='Имя програмировавшего терминал не актуальна')
    sys_mon_id = Column(ForeignKey('monitoring_system.mon_sys_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ID системы мониторинга')
    contragent_id = Column(ForeignKey('Contragents.ca_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ID контрагента')
    coment = Column(String(270, 'utf8mb3_unicode_ci'), comment='Коментарии')
    itprogrammer_id = Column(ForeignKey('auth_user.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ссылается к программистам')
    device_owner = Column(TINYINT, comment='Принадлежность терминала:\\r\\n--1 МЫ\\r\\n--0 Клиент')

    contragent = relationship('Contragents', back_populates='devices')
    devices_brand = relationship('DevicesBrands', back_populates='devices')
    itprogrammer = relationship('AuthUser', back_populates='devices')
    sys_mon = relationship('MonitoringSystem', back_populates='devices')
    devices_diagnostics = relationship('DevicesDiagnostics', back_populates='device')
    sim_cards = relationship('SimCards', back_populates='sim_device')


class DevicesCommands(Base):
    __tablename__ = 'devices_commands'
    __table_args__ = {'comment': 'Таблица для хранения информации о командах для устройств не по ТЗ'}

    id = Column(Integer, primary_key=True)
    command = Column(VARCHAR(100), comment='сама команда')
    device_brand = Column(ForeignKey('devices_brands.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Id брэнда терминала')
    method = Column(VARCHAR(10), comment='тип отправки команды\\r\\n0 - смс\\r\\n1 - интернет\\r\\n2 - любым')
    description = Column(VARCHAR(300), comment='описание действия команды')

    devices_brands = relationship('DevicesBrands', back_populates='devices_commands')


class DiscountClientLink(Base):
    __tablename__ = 'discount_client_link'
    __table_args__ = {'comment': 'Связка клиент скидки для клиентов'}

    dis_cl_link_id = Column(Integer, primary_key=True, comment='ID связи')
    cl_id = Column(ForeignKey('Contragents.ca_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='ID клиента')
    dis_id = Column(ForeignKey('discount_client.dis_cl_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='ID скидки')

    cl = relationship('Contragents', back_populates='discount_client_link')
    dis = relationship('DiscountClient', back_populates='discount_client_link')


class EquipmentWarehouse(Base):
    __tablename__ = 'equipment_warehouse'
    __table_args__ = {'comment': 'Таблица склада'}

    id_unit = Column(BigInteger, primary_key=True, comment='Идентификатор записи')
    add_date = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Время регистрации добавления товара на склад')
    serial_number = Column(String(200, 'utf8mb3_unicode_ci'), nullable=False, unique=True, comment='Серийный номер')
    availability = Column(TINYINT(1), nullable=False, server_default=text("'1'"), comment='Наличие на складе\\r\\n0- нет в наличии\\r\\n1- в наличии')
    whom_issued = Column(String(300, 'utf8mb3_unicode_ci'), nullable=False, comment='Кому выдан')
    affiliation = Column(TINYINT, nullable=False, comment='Принадлежность к подразделению:\\r\\n0-Сервис\\r\\n1- мониторинг')
    terminal_model_id = Column(ForeignKey('devices_brands.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Реляционный id device')
    sensor_id = Column(ForeignKey('sensor_brands.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Реляция id к датчикам')
    delivery_date = Column(DateTime, comment='Дата выдачи')
    client_id = Column(ForeignKey('Contragents.ca_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Клиент как в 1С')
    comment = Column(VARCHAR(300), comment='коментарий')

    client = relationship('Contragents', back_populates='equipment_warehouse')
    sensor = relationship('SensorBrands', back_populates='equipment_warehouse')
    terminal_model = relationship('DevicesBrands', back_populates='equipment_warehouse')


class ObjectSensors(Base):
    __tablename__ = 'object_sensors'
    __table_args__ = {'comment': 'Датчик'}

    sensor_id = Column(Integer, primary_key=True)
    sensor_type = Column(TINYINT, nullable=False, comment='Тип датчика:\\r\\n1ДУТ, 2Температуры3наклона')
    sensor_technology = Column(TINYINT, nullable=False, comment='Подтип датчика:\\r\\n1аналоговый,2цифровой,\\r\\n3частотный')
    sensor_model_id = Column(ForeignKey('sensor_brands.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Модель датчика к моделям')
    sensor_connect_type = Column(VARCHAR(255), comment='Тип подключения')
    client_id = Column(ForeignKey('Contragents.ca_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Связь с id Клиента')
    sensor_serial = Column(String(100, 'utf8mb3_unicode_ci'), unique=True, comment='Серийный номер датчика')
    name_installer = Column(String(150, 'utf8mb3_unicode_ci'), comment='Имя монтажника')
    installer_id = Column(Integer, comment='Id монтажника')

    client = relationship('Contragents', back_populates='object_sensors')
    sensor_model = relationship('SensorBrands', back_populates='object_sensors')


class SenderLogger(Base):
    __tablename__ = 'sender_logger'
    __table_args__ = {'comment': 'Таблица с рассылками'}

    send_id = Column(Integer, primary_key=True)
    send_time = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Время события рассылки')
    send_mail = Column(String(20, 'utf8mb3_unicode_ci'), comment='Почта рассылки')
    send_client_id = Column(ForeignKey('Contragents.ca_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Ид клиента БД_2')
    send_client_id_okdesk = Column(Integer, comment='ID клиента ОКДЕСК')
    send_req_okdesk_id = Column(Integer, comment='ID заявки в окдеск')
    send_text = Column(LONGTEXT, comment='Текст рассылки')

    send_client = relationship('Contragents', back_populates='sender_logger')


class DevicesDiagnostics(Base):
    __tablename__ = 'devices_diagnostics'
    __table_args__ = {'comment': 'Таблица для хранения информации о диагностике устройств не по тз'}

    id = Column(Integer, primary_key=True)
    device_id = Column(ForeignKey('devices.device_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Отношение к терминалам')
    programmer_id = Column(ForeignKey('auth_user.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Отношение к программистам')
    brought = Column(TINYINT, nullable=False, comment='Принесён:\\r\\n0-от клиента\\r\\n1-после ремонта')
    comment = Column(String(300, 'utf8mb3_unicode_ci'), nullable=False, comment='Коментарий')
    accept_date = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Дата приёма')
    transfer_date = Column(DateTime, comment='Дата передачи')
    whom_tranfer = Column(TINYINT, comment='Куда отдан:\\r\\n0 - клиенту\\r\\n1 - в ремонт')

    device = relationship('Devices', back_populates='devices_diagnostics')
    programmer = relationship('AuthUser', back_populates='devices_diagnostics')


class DiscountObjLink(Base):
    __tablename__ = 'discount_obj_link'

    dis_obj_link_id = Column(Integer, primary_key=True)
    obj_id = Column(ForeignKey('ca_objects.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='ID объекта')
    dis_id = Column(ForeignKey('discount_obj.dis_obj_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='ID скидки под объекты')

    dis = relationship('DiscountObj', back_populates='discount_obj_link')
    obj = relationship('CaObjects', back_populates='discount_obj_link')


class GroupObjectRetrans(Base):
    __tablename__ = 'group_object_retrans'
    __table_args__ = {'comment': 'Таблица для сведения объектов и ретрансляторов'}

    id_group = Column(Integer, primary_key=True, comment='Айдишник')
    obj_id = Column(ForeignKey('ca_objects.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Айдишник объекта')
    retr_id = Column(ForeignKey('object_retranslators.retranslator_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Айдишник ретранслятора')

    obj = relationship('CaObjects', back_populates='group_object_retrans')
    retr = relationship('ObjectRetranslators', back_populates='group_object_retrans')


class InfoServObj(Base):
    __tablename__ = 'info_serv_obj'
    __table_args__ = {'comment': 'Объекты с информационными сервисами'}

    serv_obj_id = Column(Integer, primary_key=True, comment='ID подписки')
    serv_obj_sys_mon_id = Column(ForeignKey('ca_objects.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Внутренний ID объекта\\r\\nБазы данных из СМ')
    info_obj_serv_id = Column(ForeignKey('information_services.serv_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='ID ведёт сервисам')
    subscription_start = Column(DateTime, nullable=False, comment='Время начала подписки')
    service_counter = Column(Integer, nullable=False, comment='СЧЁТЧИК услуг\\r\\n0- мгновенно\\r\\n1-раз в день\\r\\n2-раз в неделю\\r\\n3-раз в месяц')
    stealth_type = Column(TINYINT, nullable=False, comment='0 - автоматический\\r\\n1 - с проверкой')
    monitoring_sys = Column(ForeignKey('monitoring_system.mon_sys_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='Система мониторинга')
    sys_id_obj = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='ID объекта в системе мониторинга')
    sys_login = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='Логин пользователя от системы мониторинга')
    sys_password = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='Пароль пользователя от СМ')
    subscription_end = Column(DateTime, comment='Время окончания подписки')
    tel_num_user = Column(VARCHAR(11), comment='Телефонный номер с которого созданна услуга')
    send_meth = Column(TINYINT, comment='Способ отправки 0 - ОКДЕСК\\r\\n1 - MAIL')

    info_obj_serv = relationship('InformationServices', back_populates='info_serv_obj')
    monitoring_system = relationship('MonitoringSystem', back_populates='info_serv_obj')
    serv_obj_sys_mon = relationship('CaObjects', back_populates='info_serv_obj')


class ObjectVehicles(Base):
    __tablename__ = 'object_vehicles'
    __table_args__ = {'comment': 'Таблица для хранения информации об объектах-транспортных '
                'средствах'}

    vehicle_id = Column(Integer, primary_key=True)
    vehicle_gos_nomer = Column(VARCHAR(25), nullable=False, unique=True, comment='госномер')
    vehicle_object_id = Column(ForeignKey('ca_objects.id'), index=True, comment='привязка к объекту')
    vehicle_ca_id = Column(ForeignKey('Contragents.ca_id'), index=True, comment='привязка к контрагенту')
    vehicle_vendor_name = Column(VARCHAR(255), comment='производитель тс')
    vehicle_vendor_model = Column(VARCHAR(255), comment='марка тс')
    vehicle_year_of_manufacture = Column(VARCHAR(255), comment='дата выпуска тс')
    vehicle_gos_nomer_region = Column(VARCHAR(255), comment='регион')
    vehicle_type = Column(VARCHAR(255), comment='тип тс')
    vehicle_vin = Column(VARCHAR(255), comment='вин')

    vehicle_ca = relationship('Contragents', back_populates='object_vehicles')
    vehicle_object = relationship('CaObjects', back_populates='object_vehicles')


class ServiceSubscriptionLog(Base):
    __tablename__ = 'service_subscription_log'
    __table_args__ = {'comment': 'Лог изменений сервисных подписок'}

    log_id = Column(Integer, primary_key=True, comment='ID записи лога')
    user_id = Column(ForeignKey('auth_user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='ID пользователя')
    username = Column(VARCHAR(150), nullable=False, comment='Имя пользователя')
    object_id = Column(ForeignKey('ca_objects.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='ID объекта')
    action = Column(VARCHAR(50), nullable=False, comment='Действие')
    changes = Column(TEXT, comment='Изменения в JSON')
    change_time = Column(DateTime, index=True, server_default=text('CURRENT_TIMESTAMP'), comment='Время изменения')

    object = relationship('CaObjects', back_populates='service_subscription_log')
    user = relationship('AuthUser', back_populates='service_subscription_log')


class SimCards(Base):
    __tablename__ = 'sim_cards'

    sim_id = Column(Integer, primary_key=True)
    sim_iccid = Column(VARCHAR(40), unique=True, comment='ICCID')
    sim_tel_number = Column(VARCHAR(40), comment='телефонный номер сим')
    client_name = Column(VARCHAR(270), comment='Имя клиента')
    sim_cell_operator = Column(ForeignKey('Cell_operator.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='Сотовый оператор(надо по ID)')
    sim_owner = Column(TINYINT(1), comment="1, 'Мы'\\r\\n0, 'Клиент'")
    sim_device_id = Column(ForeignKey('devices.device_id'), index=True, comment='ID к девайсам(devices)')
    sim_date = Column(DateTime, comment='Дата регистрации сим')
    status = Column(Integer, comment='Активность симки:\\r\\n0-списана, 1-активна, 2-приостан, 3-первичная блокировка, 4-статус неизвестен,\\r\\n5 - Сезонная блокировка')
    terminal_imei = Column(String(25, 'utf8mb3_unicode_ci'), comment='IMEI терминала в который вставлена симка')
    contragent_id = Column(ForeignKey('Contragents.ca_id', ondelete='SET NULL', onupdate='SET NULL'), index=True, comment='ID контрагента')
    ca_uid = Column(String(100, 'utf8mb3_unicode_ci'), comment='Уникальный id контрагента')
    itprogrammer_id = Column(ForeignKey('auth_user.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ID сотрудника програмировавшего терминал')
    block_start = Column(DateTime, comment='Начало блокировки')
    block_end = Column(DateTime, comment='Предварительный конец блокировки')

    contragent = relationship('Contragents', back_populates='sim_cards')
    itprogrammer = relationship('AuthUser', back_populates='sim_cards')
    Cell_operator = relationship('CellOperator', back_populates='sim_cards')
    sim_device = relationship('Devices', back_populates='sim_cards')
    billing = relationship('Billing', back_populates='sim')


class Billing(Base):
    __tablename__ = 'billing'
    __table_args__ = {'comment': 'Таблица снимок параметров билинга за день'}

    bil_id = Column(Integer, primary_key=True, comment='ID билинга')
    sys_mon_id = Column(ForeignKey('monitoring_system.mon_sys_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='ID системы мониторинга')
    sys_mon_price = Column(Integer, nullable=False, comment='Стоимость СМ для КЛ')
    obj_id = Column(ForeignKey('ca_objects.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='ID объекта в БД')
    obj_name = Column(VARCHAR(100), nullable=False, comment='Название объекта')
    obj_status_id = Column(ForeignKey('object_statuses.status_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='ID статуса объекта')
    record_time = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='Время создания записи')
    obj_status_name = Column(String(50, 'utf8mb3_unicode_ci'), nullable=False, comment='Имя статуса объекта')
    obj_group_id = Column(String(400, 'utf8mb3_unicode_ci'), nullable=False, comment='ИД группы объектов')
    obj_id_in_sys = Column(String(300, 'utf8mb3_unicode_ci'), nullable=False, comment='ID объекта в системе мониторинга')
    sys_mon_name = Column(String(100, 'utf8mb3_unicode_ci'), nullable=False, comment='Название системы мониторинга')
    retrans_id = Column(ForeignKey('object_retranslators.retranslator_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ID ретрансляции')
    retrans_name = Column(String(50, 'utf8mb3_unicode_ci'), comment='Название ретрансляции')
    retrans_price = Column(Integer, comment='Цена ретрансляции')
    sim_id = Column(ForeignKey('sim_cards.sim_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ID СИМКАРТЫ')
    sim_operat_name = Column(String(50, 'utf8mb3_unicode_ci'), comment='Имя оператора')
    sim_price = Column(Integer, comment='Цена сим для КЛ')
    client_id = Column(ForeignKey('Contragents.ca_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True, comment='ID клиента')
    client_name = Column(String(300, 'utf8mb3_unicode_ci'), comment='Имя клиента')
    client_inn = Column(String(200, 'utf8mb3_unicode_ci'), comment='ИНН Клиента')
    discount_client = Column(JSON, comment="СКИДКИ КЛИЕНТА\\r\\n[{'dis_id': 1, 'dis_name': 'Лояльность'},\\r\\n {'dis_id': 2, 'dis_name': 'Кол-во объектов > 50'},\\r\\n]")
    discount_client_rate = Column(Integer, comment='Итоговый процент Скидки')
    discount_obj = Column(JSON, comment="СКИДКИ КЛИЕНТА [{'dis_id': 1, 'dis_name': 'Лояльность'}, {'dis_id': 2, 'dis_name': 'Дружественный'}, ]")
    discount_obj_rate = Column(Integer, comment='Процент скидок на объект')
    obj_group_name = Column(VARCHAR(400), comment='Название группы объектов как в СМ')
    client_login = Column(VARCHAR(400), comment='Логин клиента')
    client_kpp = Column(String(200, 'utf8mb3_unicode_ci'), comment='Клиентский КПП')
    total_sum = Column(Integer, comment='Итоговая сумма')
    obj_imei = Column(String(100, 'utf8mb3_unicode_ci'), comment='IMEI объекта')

    client = relationship('Contragents', back_populates='billing')
    obj = relationship('CaObjects', back_populates='billing')
    obj_status = relationship('ObjectStatuses', back_populates='billing')
    retrans = relationship('ObjectRetranslators', back_populates='billing')
    sim = relationship('SimCards', back_populates='billing')
    sys_mon = relationship('MonitoringSystem', back_populates='billing')
