# Todue-list-api

TodoリストアプリのバックエンドAPI（FastAPI + Supabase）

## セットアップ

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

`.env`ファイルを作成し、以下の環境変数を設定してください：

```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

### 3. Supabaseデータベースのセットアップ

Supabaseで以下のテーブルを作成してください：

```sql
CREATE TABLE items (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  kind TEXT NOT NULL,
  date TEXT NOT NULL,
  score INTEGER NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### 4. サーバーの起動

```bash
uvicorn main:app --reload
```

APIドキュメントは `http://localhost:8000/docs` で確認できます。

## APIエンドポイント

- `GET /` - ルートエンドポイント
- `GET /items/` - 全Todoアイテムを取得
- `GET /items/{item_id}` - 特定のTodoアイテムを取得
- `POST /items/` - 新しいTodoアイテムを追加
- `PATCH /items/{item_id}` - Todoアイテムを更新