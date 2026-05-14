create table if not exists spatial_zones (
  zone_id text primary key,
  city text not null,
  name text not null,
  local_roi_score numeric not null
);

