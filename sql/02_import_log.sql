--  создание журнала (история) загрузок данных реестра отгрузок ОНОС
create schema if not exists onos;

create table if not exists onos.import_log (
  id         bigserial primary key,
  file_name  text not null unique,
  loaded_at  timestamptz not null default now(),
  rows_count integer not null default 0,
  note       text
);
