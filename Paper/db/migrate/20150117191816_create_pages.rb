class CreatePages < ActiveRecord::Migration
  def change
    create_table :pages do |t|
      t.string :html
      t.string :color
      t.integer :height
      t.integer :width
      t.integer :mLeft
      t.integer :mTop

      t.timestamps null: false
    end
  end
end
