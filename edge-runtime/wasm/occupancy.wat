(module
  (func (export "normalize") (param $value f32) (result f32)
    local.get $value
    f32.const 100
    f32.div))

