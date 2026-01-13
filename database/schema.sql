-- 1. Transactions Table (Ausgaben/Einnahmen)
CREATE TABLE public.transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    amount DECIMAL(10,2) NOT NULL, -- Betrag (Negativ für Ausgaben, Positiv für Einnahmen möglich, oder separate Spalte)
    category TEXT NOT NULL,        -- z.B. 'Lebensmittel', 'Miete', 'Gehalt'
    description TEXT,              -- Details: 'Einkauf Rewe'
    date DATE NOT NULL,            -- Wann passiert?
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 2. Optional: Budgets (Ziele)
CREATE TABLE public.budgets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category TEXT NOT NULL,
    limit_amount DECIMAL(10,2) NOT NULL,
    month DATE NOT NULL -- z.B. '2023-01-01' für Januar 2023
);

-- RLS (Row Level Security) aktivieren - Sicherheit!
ALTER TABLE public.transactions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.budgets ENABLE ROW LEVEL SECURITY;

-- Policy (Dient hier als Beispiel, standardmäßig full access für authentifizierten Service Role Key)
CREATE POLICY "Enable all access for service role" ON public.transactions
    FOR ALL
    TO service_role
    USING (true)
    WITH CHECK (true);
