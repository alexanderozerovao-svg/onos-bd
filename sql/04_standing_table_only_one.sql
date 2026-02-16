create table if not exists onos.reestr_shipments_stage
(like onos.reestr_shipments including defaults);

-- staging хранит сырые загрузки, row_hash тут можно не уникализировать
