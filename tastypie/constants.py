from __future__ import unicode_literals

# Enable all basic ORM filters but do not allow filtering across relationships.
ALL = 1
# Enable all ORM filters, including across relationships
ALL_WITH_RELATIONS = 2

# Valid query types (a set is used for speedy lookups). These are (currently)
# considered SQL-specific; other storage systems may choose to use different
# lookup types.
QUERY_TERMS = {
    'exact', 'iexact', 'contains', 'icontains', 'gt', 'gte', 'lt', 'lte', 'in',
    'startswith', 'istartswith', 'endswith', 'iendswith', 'range', 'year',
    'month', 'day', 'week_day', 'hour', 'minute', 'second', 'isnull', 'search',
    'regex', 'iregex',
}
