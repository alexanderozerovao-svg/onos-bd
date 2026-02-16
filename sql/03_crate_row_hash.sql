-- для каждой строки считаем “отпечаток” (hash) по ключевым полям и запрещаем вставку одинаковых строк.
alter table onos.reestr_shipments
add column if not exists row_hash text;

create unique index if not exists ux_reestr_row_hash
on onos.reestr_shipments(row_hash);
