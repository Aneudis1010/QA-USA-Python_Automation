URBAN_ROUTES_URL = "https://cnt-70cb7558-6135-4885-a0b0-14f23b32c181.containerhub.tripleten-services.com/"
BASE_URL = URBAN_ROUTES_URL

FROM_ADDRESS = "East 2nd Street, 601"
TO_ADDRESS = "1300 1st St"

PHONE_NUMBER = "+1 123 123 12 12"

# 🔴 REQUIRED for tests — was missing
PHONE_CODE = "1234"

# ✅ Valid test card (passes UI validation)
CARD_NUMBER = "4242 4242 4242 4242"
CARD_CODE = "123"

# 🔴 Your tests likely expect COMMENT, not DRIVER_COMMENT
COMMENT = "Stop at the juice bar, please"

# (Optional — safe alias if some tests still use old name)
DRIVER_COMMENT = COMMENT
