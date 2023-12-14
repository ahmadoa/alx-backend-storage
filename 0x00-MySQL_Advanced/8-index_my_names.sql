-- 8. Optimize simple search
-- creates index idx_name_first on table
-- names & the first letter of name
CREATE INDEX idx_name_first ON names(name(1));
